def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for s in strings:
        if len(s) >= 3:
            key = sorted_lower(s)
            if key in anagram_counts:
                anagram_counts[key] += 1
            else:
                anagram_counts[key] = 1
    pairs_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
            if pairs_count > 17:
                return False
    return True