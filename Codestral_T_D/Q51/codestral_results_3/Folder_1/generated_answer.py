def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) <= 30