def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 318:
                    return False
            else:
                anagrams[sorted_string] = 1
    return True