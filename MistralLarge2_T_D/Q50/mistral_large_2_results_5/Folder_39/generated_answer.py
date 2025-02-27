from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_dict[key].append(s)
    count = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count >= 54:
                return True
    return False