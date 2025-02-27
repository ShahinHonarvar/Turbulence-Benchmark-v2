def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    pairs = sum((a * (a - 1) // 2 for a in anagrams.values()))
    return pairs <= 44