from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_counts.values():
        pairs = len(group) * (len(group) - 1) // 2
        anagram_pairs += pairs
    return anagram_pairs >= 35