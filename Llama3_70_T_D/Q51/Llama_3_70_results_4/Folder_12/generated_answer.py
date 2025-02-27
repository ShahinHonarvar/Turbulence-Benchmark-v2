def if_contains_anagrams(strs):
    anagram_count = {}
    for s in strs:
        s = ''.join(sorted((c for c in s.lower() if c.isalpha())))
        if len(s) < 3:
            continue
        anagram_count[s] = anagram_count.get(s, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 92