from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    for key, values in anagram_dict.items():
        if len(values) > 1:
            count += len(values) * (len(values) - 1) // 2
        if count > 81:
            return False
    return True