def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3 and sorted_s.isalpha():
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return count <= 416