def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            anagrams[s] = anagrams.get(s, 0) + 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values() if n > 1))
    return count <= 58