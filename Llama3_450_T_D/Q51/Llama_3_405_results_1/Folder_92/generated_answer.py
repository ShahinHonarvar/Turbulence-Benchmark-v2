def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs <= 34