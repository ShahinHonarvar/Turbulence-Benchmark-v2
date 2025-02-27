def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3 or not s_lower.isalpha():
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 173