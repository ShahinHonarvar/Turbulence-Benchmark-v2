def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values() if len(string) >= 3))
    return count <= 30