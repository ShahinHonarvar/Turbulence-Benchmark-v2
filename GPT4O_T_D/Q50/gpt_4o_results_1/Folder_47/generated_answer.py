from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str] += 1
    count = 0
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
        if count >= 47:
            return True
    return False