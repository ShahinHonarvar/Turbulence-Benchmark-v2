def if_contains_anagrams(list_of_strings):
    list_of_strings = [''.join(filter(str.isalpha, string)).lower() for string in list_of_strings if len(''.join(filter(str.isalpha, string))) >= 3]
    anagrams = {}
    count = 0
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            count += anagrams[sorted_string]
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return count <= 70