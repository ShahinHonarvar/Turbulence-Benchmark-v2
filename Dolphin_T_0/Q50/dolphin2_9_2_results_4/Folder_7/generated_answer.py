def if_contains_anagrams(list_of_strings):
    anagrams_found = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                if set(list_of_strings[i].lower()) == set(list_of_strings[j].lower()):
                    anagrams_found += 1
    return anagrams_found >= 178