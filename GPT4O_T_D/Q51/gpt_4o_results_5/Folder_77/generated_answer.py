def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_counts[sorted_s] = anagram_counts.get(sorted_s, 0) + 1
    count = 0
    for value in anagram_counts.values():
        if value > 1:
            pairs = value * (value - 1) // 2
            count += pairs
            if count > 17:
                return False
    return True