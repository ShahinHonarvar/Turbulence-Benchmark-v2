def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    num_anagrams = sum([v * (v - 1) // 2 for v in anagrams.values() if v > 1])
    return num_anagrams <= 423