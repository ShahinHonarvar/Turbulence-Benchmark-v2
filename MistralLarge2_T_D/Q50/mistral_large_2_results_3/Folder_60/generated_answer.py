from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = defaultdict(int)
    pairs = 0
    for word in words:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        count[norm_word] += 1
    for v in count.values():
        pairs += v * (v - 1) // 2
    return pairs >= 60