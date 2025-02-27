def if_contains_anagrams(list_of_strings):
    anagram_pairs = []
    for string in list_of_strings:
        for other_string in list_of_strings:
            if string != other_string and len(string) >= 3 and (len(other_string) >= 3) and (string.lower() == other_string.lower()):
                anagram_pairs.append((string, other_string))
    return len(anagram_pairs) <= 97