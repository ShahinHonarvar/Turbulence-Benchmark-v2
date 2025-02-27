def if_contains_anagrams(string_list):
    anagram_counts = {}
    for s in string_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_counts:
            anagram_counts[sorted_str] += 1
        else:
            anagram_counts[sorted_str] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values() if count > 1))
    return anagram_pairs >= 143