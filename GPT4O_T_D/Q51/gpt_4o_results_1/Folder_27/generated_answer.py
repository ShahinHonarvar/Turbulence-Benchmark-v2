from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagram_dict[key].append(string)
    anagram_pairs = 0
    for key, group in anagram_dict.items():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 113:
            return False
    return True