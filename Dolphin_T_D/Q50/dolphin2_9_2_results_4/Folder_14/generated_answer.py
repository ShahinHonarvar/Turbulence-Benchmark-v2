def if_contains_anagrams(list_strings):
    anagrams = 0
    for i in range(len(list_strings)):
        for j in range(i + 1, len(list_strings)):
            if len(list_strings[i]) >= 3 and len(list_strings[j]) >= 3:
                if sorted(list_strings[i].lower()) == sorted(list_strings[j].lower()):
                    anagrams += 1
                    if anagrams >= 22:
                        return True
    return False