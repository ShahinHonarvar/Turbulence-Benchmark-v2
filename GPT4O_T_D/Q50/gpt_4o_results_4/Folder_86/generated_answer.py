def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_counts:
                anagram_counts[sorted_str] += 1
            else:
                anagram_counts[sorted_str] = 1
    pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs += count * (count - 1) // 2
        if pairs >= 115:
            return True
    return False