from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        cleaned = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(cleaned) >= 3:
            anagram_dict[cleaned].append(string)
    anagram_pairs = 0
    for words in anagram_dict.values():
        n = len(words)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 18:
            return False
    return True