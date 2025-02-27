def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            key = ''.join(sorted(word))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    pairs = sum(anagrams.values())
    return pairs <= 92