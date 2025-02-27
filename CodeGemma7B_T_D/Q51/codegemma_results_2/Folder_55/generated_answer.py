from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_counts = defaultdict(int)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower().replace(' ', '')))
        if len(sorted_str) >= 3:
            anagram_counts[sorted_str] += 1
    return sum((count ** 2 <= 44 for count in anagram_counts.values())) >= len(anagram_counts)