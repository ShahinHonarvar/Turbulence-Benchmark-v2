from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    normalized_words = [normalize(word) for word in words if len(word) >= 3]
    seen = Counter()
    for word in normalized_words:
        if seen[word] > 0:
            anagram_pairs += seen[word]
        seen[word] += 1
    return anagram_pairs <= 39