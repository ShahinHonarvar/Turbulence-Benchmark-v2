from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_count[sorted_string] += 1
    pairs = sum(((count - 1) * count // 2 for count in anagram_count.values()))
    return pairs <= 28