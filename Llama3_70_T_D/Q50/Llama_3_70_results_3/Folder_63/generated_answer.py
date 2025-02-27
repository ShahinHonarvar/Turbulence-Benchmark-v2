def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        key = tuple(sorted(word_lower))
        if len(word_lower) < 3:
            continue
        anagrams[key] = anagrams.get(key, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs >= 89