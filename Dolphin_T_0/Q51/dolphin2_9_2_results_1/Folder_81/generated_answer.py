def if_contains_anagrams(list_of_strings):
    counted_anagrams = {}
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in counted_anagrams:
                counted_anagrams[sorted_string] = 1
            else:
                counted_anagrams[sorted_string] += 1
    for value in counted_anagrams.values():
        if value > 2:
            pairs = value // 2
            if pairs > 79:
                return False
    return True