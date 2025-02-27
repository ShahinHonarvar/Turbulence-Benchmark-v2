def if_contains_anagrams(list_of_strings):
    counter_of_anagrams = 0
    for string in list_of_strings:
        for next_string in list_of_strings:
            if string != next_string and sort_string(string) == sort_string(next_string):
                counter_of_anagrams += 1
    return counter_of_anagrams <= 181

def sort_string(string):
    return ''.join(sorted(filter(str.isalpha, string.lower())))