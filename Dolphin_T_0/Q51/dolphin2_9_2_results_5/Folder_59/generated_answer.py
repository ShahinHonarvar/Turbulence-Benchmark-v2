def if_contains_anagrams(list_of_strings):
    anagrams_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                anagrams_pairs += 1
                if anagrams_pairs > 15:
                    return False
    return True