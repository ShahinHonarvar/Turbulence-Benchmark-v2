from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    normalized_words = [normalize(word) for word in words if len(word) >= 3]
    freq = Counter(normalized_words)
    pairs_count = sum((v * (v - 1) // 2 for v in freq.values()))
    return pairs_count <= 93