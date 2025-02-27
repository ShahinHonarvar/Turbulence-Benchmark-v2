def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        s_lower = ''.join(sorted(s.lower()))
        if s_lower in anagrams:
            anagrams[s_lower].append(s)
        else:
            anagrams[s_lower] = [s]
    count = 0
    for a in anagrams.values():
        count += len(a) * (len(a) - 1) // 2
        if count >= 194:
            return True
    return False