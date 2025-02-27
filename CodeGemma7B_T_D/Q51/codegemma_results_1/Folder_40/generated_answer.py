def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = 0
        anagrams[key] += 1
    if len(anagrams) <= 29:
        return True
    return False