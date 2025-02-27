def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string in anagrams:
            count += 1
        anagrams[sorted_string] = True
    return count >= 66