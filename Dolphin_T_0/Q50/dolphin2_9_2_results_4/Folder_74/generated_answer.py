def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for string in list_of_strings:
        if len(string) >= 3:
            for other_string in list_of_strings:
                if sorted(string.lower()) == sorted(other_string.lower()) and string != other_string:
                    anagram_pairs += 1
    return anagram_pairs >= 17