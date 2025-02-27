def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 1
            else:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] == 2:
                    anagrams_count += 1
    return anagrams_count >= 140