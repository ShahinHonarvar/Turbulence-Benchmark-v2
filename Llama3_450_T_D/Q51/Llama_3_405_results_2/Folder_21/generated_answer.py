def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str.isalpha():
            anagrams[sorted_str] = anagrams.get(sorted_str, 0) + 1
    count = sum((1 for value in anagrams.values() if value > 1))
    return count <= 26