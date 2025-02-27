def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for string in list_of_strings:
        if len(string) >= 3:
            string = string.lower()
            for second_string in list_of_strings:
                if len(second_string) >= 3 and only_lowercase_string == sorted(second_string.lower()) and (string != second_string):
                    anagram_pairs += 1
    return anagram_pairs >= 219