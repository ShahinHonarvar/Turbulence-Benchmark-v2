def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagrams.add(sorted_str)
    return len(anagrams) <= 98