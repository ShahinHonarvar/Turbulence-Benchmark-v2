from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 43