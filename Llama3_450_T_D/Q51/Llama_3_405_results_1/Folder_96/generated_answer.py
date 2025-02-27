def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(set((c for c in s.lower() if c.isalpha()))))
        if len(sorted_str) < 3:
            continue
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count <= 2