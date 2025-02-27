def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        string = ''.join((ch.lower() for ch in string if ch.isalpha()))
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] > 50:
                return False
        else:
            anagrams[sorted_string] = 1
    return True