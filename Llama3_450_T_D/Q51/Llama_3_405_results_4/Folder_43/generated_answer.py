def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            anagram_count[sorted_str] = anagram_count.get(sorted_str, 0) + 1
    count = sum((c // 2 for c in anagram_count.values() if c > 1))
    return count <= 3