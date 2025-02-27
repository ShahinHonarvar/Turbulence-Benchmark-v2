def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 78