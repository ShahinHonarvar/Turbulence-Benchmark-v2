def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    anagram_pairs = sum([len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()])
    return anagram_pairs <= 85