def if_contains_anagrams(list_of_strings):
    anagrams = 0
    for i in range(0, len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) < 3 or len(list_of_strings[j]) < 3:
                continue
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                anagrams += 1
                if anagrams > 52:
                    return False
    return anagrams <= 52