def if_contains_anagrams(list_of_strings):
    count_anagrams = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) == len(list_of_strings[j]) and len(list_of_strings[i]) >= 3:
                if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                    count_anagrams += 1
    if count_anagrams >= 29:
        return True
    else:
        return False