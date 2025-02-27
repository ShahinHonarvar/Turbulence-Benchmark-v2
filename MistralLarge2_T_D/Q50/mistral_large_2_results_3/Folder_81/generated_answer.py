from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_count.values():
        if len(group) > 1:
            anagram_pairs += len(group) - 1
    return anagram_pairs >= 16