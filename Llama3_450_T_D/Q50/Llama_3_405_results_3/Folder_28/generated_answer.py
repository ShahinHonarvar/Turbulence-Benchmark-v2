def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]
    pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return pairs >= 81