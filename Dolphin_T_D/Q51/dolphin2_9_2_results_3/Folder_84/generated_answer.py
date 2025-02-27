def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return len([pair for pair in anagrams.values() if pair > 1]) <= 16