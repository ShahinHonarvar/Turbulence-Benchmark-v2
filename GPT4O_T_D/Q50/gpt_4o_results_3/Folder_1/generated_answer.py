from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_dict[key] += 1
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 96