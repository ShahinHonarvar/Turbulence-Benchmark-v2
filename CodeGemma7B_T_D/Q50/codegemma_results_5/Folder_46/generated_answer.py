def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        string = string.lower().replace(' ', '')
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = 0
    for value in anagrams.values():
        count += int(value / 2)
    if count >= 38:
        return True
    else:
        return False