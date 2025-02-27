import itertools

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    pair_count = sum((1 for v in anagrams.values() if len(v) > 1))
    return pair_count >= 39