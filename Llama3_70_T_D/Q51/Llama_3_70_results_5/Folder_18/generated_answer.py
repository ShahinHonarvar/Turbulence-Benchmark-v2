def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        s_sorted = ''.join(sorted((c for c in s_lower if c.isalpha())))
        if len(s_sorted) >= 3:
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 42