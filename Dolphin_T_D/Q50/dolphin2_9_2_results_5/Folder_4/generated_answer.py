def if_contains_anagrams(list_of_strings):
    anagrams_found = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                if list_of_strings[i].lower() == list_of_strings[j].lower() and sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    anagrams_found += 1
    if anagrams_found >= 84:
        return True
    else:
        return False