from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(lambda: [])
    for string in strings:
        clean_string = ''.join(filter(str.isalpha, string)).lower()
        if len(clean_string) >= 3:
            sorted_string = ''.join(sorted(clean_string))
            anagram_map[sorted_string].append(clean_string)
    anagram_pairs = 0
    for anagrams in anagram_map.values():
        if len(anagrams) > 1:
            anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs <= 42