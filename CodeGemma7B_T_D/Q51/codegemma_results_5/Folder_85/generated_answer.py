from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for word in string_list:
        normalized_word = ''.join(sorted(word.lower()))
        if len(normalized_word) >= 3:
            anagrams[normalized_word].append(word)
    pairs = 0
    for anagram_list in anagrams.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) / 2
    return pairs <= 276