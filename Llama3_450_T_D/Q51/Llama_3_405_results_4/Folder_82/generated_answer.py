def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagram_count[sorted_str] = anagram_count.get(sorted_str, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 40