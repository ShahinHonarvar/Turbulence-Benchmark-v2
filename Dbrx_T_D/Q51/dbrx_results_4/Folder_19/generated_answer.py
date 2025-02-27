def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] > 69:
                return False
        else:
            anagrams[sorted_string] = 1
    return True