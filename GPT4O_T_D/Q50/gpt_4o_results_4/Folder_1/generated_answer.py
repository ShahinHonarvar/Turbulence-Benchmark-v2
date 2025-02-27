from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        lower_str = string.lower()
        for i in range(len(lower_str) - 2):
            sorted_substring = ''.join(sorted(lower_str[i:i + 3]))
            anagram_dict[sorted_substring] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pair_count >= 96