from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str] += 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 41:
            return True
    return False