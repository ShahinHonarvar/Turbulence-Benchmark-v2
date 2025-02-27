def if_contains_anagrams(strs):
    anagrams = {}
    for string in strs:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    return len(anagrams) <= 69