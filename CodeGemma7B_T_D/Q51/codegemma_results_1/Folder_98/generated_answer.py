def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        s_sorted = ''.join(sorted(s.lower()))
        anagrams[s_sorted] = anagrams.get(s_sorted, []) + [s]
    return len(anagrams) <= 46