def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                sorted_string1 = sorted(list_of_strings[i].lower())
                sorted_string2 = sorted(list_of_strings[j].lower())
                if sorted_string1 == sorted_string2:
                    anagram_pairs += 1
    return anagram_pairs <= 3