from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c = Counter(word)
            key = ''.join(c.elements())
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    pairs = 0
    for k, v in anagrams.items():
        pairs += v * (v - 1) // 2
    return pairs <= 92