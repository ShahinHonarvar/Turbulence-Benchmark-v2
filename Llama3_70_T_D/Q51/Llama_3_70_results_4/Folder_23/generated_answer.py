def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        s = ''.join(filter(str.isalpha, s))
        if len(s) < 3:
            continue
        s = ''.join(sorted(s))
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    anagram_count = sum([v * (v - 1) // 2 for v in anagrams.values()])
    return anagram_count <= 49