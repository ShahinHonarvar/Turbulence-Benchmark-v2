def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagram_counts:
                anagram_counts[sorted_str] += 1
            else:
                anagram_counts[sorted_str] = 1
    total_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return total_pairs >= 91