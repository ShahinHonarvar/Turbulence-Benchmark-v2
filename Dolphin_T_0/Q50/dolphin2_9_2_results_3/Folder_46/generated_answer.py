def if_contains_anagrams(list_of_strings):
    counter_of_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                str1 = list_of_strings[i].lower()
                str2 = list_of_strings[j].lower()
                if sorted(str1) == sorted(str2):
                    counter_of_pairs += 1
    return counter_of_pairs >= 38