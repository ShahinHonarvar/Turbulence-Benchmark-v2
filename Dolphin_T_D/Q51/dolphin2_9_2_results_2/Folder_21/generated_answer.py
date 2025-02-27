def if_contains_anagrams(strings):
    anagrams = [''.join(sorted(s.lower())).rstrip('') for s in strings if len(s) >= 3]
    return len(set([frozenset(a) for a in anagrams])) <= 26