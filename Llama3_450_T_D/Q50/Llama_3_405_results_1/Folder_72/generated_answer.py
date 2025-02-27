def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_counts:
            anagram_counts[sorted_s] += 1
        else:
            anagram_counts[sorted_s] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values() if count > 1))
    return pairs >= 55