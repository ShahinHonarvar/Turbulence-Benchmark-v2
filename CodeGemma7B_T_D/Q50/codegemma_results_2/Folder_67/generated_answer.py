def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.setdefault(sorted_string, []).append(string)
    for values in anagrams.values():
        if len(values) >= 41:
            return True
    return False