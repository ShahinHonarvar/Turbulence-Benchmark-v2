def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pairs <= 181