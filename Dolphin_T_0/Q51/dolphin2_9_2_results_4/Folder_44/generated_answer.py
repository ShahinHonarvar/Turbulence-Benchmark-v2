def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                if sorted(list(list_of_strings[i].lower())) == sorted(list(list_of_strings[j].lower())):
                    anagrams_count += 1
                    if anagrams_count >= 75:
                        return True
    return False