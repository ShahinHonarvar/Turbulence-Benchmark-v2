from collections import defaultdict

def if_contains_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_map[sorted_word].append(word)
    anagram_count = 0
    for key in anagram_map:
        if len(anagram_map[key]) > 1:
            anagram_count += 1
    return anagram_count <= 11