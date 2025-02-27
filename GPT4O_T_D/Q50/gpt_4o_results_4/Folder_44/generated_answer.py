from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagrams[normalize(word)] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs_count >= 44