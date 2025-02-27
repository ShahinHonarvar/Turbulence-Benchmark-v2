def if_contains_anagrams(strings):
    anagrams = {}
    anagram_count = 0
    for s in strings:
        if len(s) < 3:
            continue
        s = s.lower()
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    for value in anagrams.values():
        if value > 1:
            anagram_count += value * (value - 1) // 2
    return anagram_count >= 41