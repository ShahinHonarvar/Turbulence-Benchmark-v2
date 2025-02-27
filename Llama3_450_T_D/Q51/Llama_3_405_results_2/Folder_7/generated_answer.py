def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = ''.join(sorted(s.lower()))
        if s_lower in anagrams and len(s) >= 3 and s.isalpha():
            anagrams[s_lower].append(s)
        elif len(s) >= 3 and s.isalpha():
            anagrams[s_lower] = [s]
    pairs = sum((len(a) * (len(a) - 1) // 2 for a in anagrams.values() if len(a) > 1))
    return pairs <= 445