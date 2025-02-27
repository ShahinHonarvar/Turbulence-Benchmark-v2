def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagram_count[sorted_str] = anagram_count.get(sorted_str, 0) + 1
    count = sum((n * (n - 1) // 2 for n in anagram_count.values() if n > 1))
    return count <= 475