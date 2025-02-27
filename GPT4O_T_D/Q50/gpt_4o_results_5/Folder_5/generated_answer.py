from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s] += 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        anagram_pairs += count * (count - 1) // 2
        if anagram_pairs >= 21:
            return True
    return False