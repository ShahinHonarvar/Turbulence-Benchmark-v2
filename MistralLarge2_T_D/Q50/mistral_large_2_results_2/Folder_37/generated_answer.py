from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = defaultdict(int)
    pairs = 0
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        pairs += count[normalized]
        count[normalized] += 1
    return pairs >= 29