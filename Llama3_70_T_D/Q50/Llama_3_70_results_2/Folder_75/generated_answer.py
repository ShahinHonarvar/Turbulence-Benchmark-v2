def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = {}
    for s in strings:
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    pairs = sum([n * (n - 1) // 2 for n in anagram_count.values() if n > 1])
    return pairs >= 70