def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] > 21:
                return False
        else:
            anagrams[sorted_string] = 1
    return True