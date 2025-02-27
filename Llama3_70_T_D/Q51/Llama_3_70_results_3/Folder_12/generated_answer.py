from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for string in lst:
        cleaned_string = ''.join(filter(str.isalpha, string)).lower()
        if len(cleaned_string) < 3:
            continue
        sorted_string = ''.join(sorted(cleaned_string))
        anagram_count[sorted_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 92