def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key] += 1
            if anagrams[key] == 14:
                return True
        else:
            anagrams[key] = 0
    return False