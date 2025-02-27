def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string in list_of_strings:
        for other_string in list_of_strings:
            if len(string) >= 3 and len(other_string) >= 3 and (string.lower() != other_string.lower()) and (sorted(string.lower()) == sorted(other_string.lower())):
                anagram_count += 1
    return anagram_count >= 21