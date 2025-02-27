def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_chars(s)
            if sorted_s in anagram_counts:
                anagram_counts[sorted_s] += 1
            else:
                anagram_counts[sorted_s] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_count <= 77