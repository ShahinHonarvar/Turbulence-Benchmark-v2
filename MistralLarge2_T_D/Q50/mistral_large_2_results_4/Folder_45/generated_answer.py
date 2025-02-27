from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagram_counts[norm_word].append(word)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_counts.values() if len(lst) > 1))
    return anagram_pairs >= 277