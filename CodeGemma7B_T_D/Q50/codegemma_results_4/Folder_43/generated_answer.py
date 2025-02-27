def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = sorted(string.lower())
        key = ''.join(sorted_string)
        if key in anagrams:
            anagrams[key] += 1
            if anagrams[key] >= 61:
                return True
        else:
            anagrams[key] = 1
    return False