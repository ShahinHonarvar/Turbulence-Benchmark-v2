from collections import defaultdict

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst]

    def sorted_str(s):
        return ''.join(sorted(s))
    anagram_dict = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            key = sorted_str(s)
            anagram_dict[key] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 88:
            return False
    return True