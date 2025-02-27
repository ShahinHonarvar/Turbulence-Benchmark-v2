def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for values in anagrams.values():
        if len(values) >= 2:
            anagram_count += len(values) * (len(values) - 1) // 2
    return anagram_count >= 36