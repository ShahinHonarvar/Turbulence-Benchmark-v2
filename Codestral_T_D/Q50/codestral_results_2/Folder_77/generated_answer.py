def if_contains_anagrams(lst):
    anagram_counts = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            anagram_counts[key] = anagram_counts.get(key, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 209