def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return sum(anagrams.values() >= 2) >= 54