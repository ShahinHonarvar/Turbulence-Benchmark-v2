from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 6