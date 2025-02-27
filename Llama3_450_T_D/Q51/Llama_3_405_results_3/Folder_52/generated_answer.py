def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 43