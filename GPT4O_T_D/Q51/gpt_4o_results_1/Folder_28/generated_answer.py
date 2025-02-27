def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = {}
    for s in strings:
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values() if count > 1))
    return total_pairs <= 78