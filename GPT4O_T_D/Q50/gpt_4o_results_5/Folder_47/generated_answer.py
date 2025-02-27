from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_dict[sorted_str] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count >= 47:
            return True
    return False