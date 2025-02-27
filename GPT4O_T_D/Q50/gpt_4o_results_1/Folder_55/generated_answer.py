from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(set)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].add(s.lower())
    for group in anagram_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count >= 15:
                return True
    return False