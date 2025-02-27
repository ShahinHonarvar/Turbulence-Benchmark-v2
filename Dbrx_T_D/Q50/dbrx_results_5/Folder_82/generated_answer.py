def if_contains_anagrams(list_strings):
    anagrams = {}
    for string in list_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    total_anagrams = sum([anagrams[key] for key in anagrams if anagrams[key] > 1])
    return total_anagrams >= 276