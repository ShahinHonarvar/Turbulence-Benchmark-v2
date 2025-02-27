from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str] += 1
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 50