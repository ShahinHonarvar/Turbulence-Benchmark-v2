def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((val * (val - 1) // 2 for val in anagrams.values())) >= 153