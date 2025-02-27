from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagram_dict[key].append(string)
    for group in anagram_dict.values():
        count += len(group) * (len(group) - 1) // 2
        if count > 74:
            return False
    return count <= 74