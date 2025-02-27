def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    for value in anagrams.values():
        if len(value) >= 2:
            count += 1
    if count >= 40:
        return True
    else:
        return False