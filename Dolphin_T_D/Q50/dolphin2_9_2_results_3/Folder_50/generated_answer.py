def if_contains_anagrams(list_of_strings):
    counter = 0
    list_of_anagrams = []
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = ''.join(sorted(list_of_strings[i].lower()))
            str2 = ''.join(sorted(list_of_strings[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                counter += 1
                list_of_anagrams.append((list_of_strings[i], list_of_strings[j]))
                if counter == 20:
                    return (True, list_of_anagrams)
    return (False, list_of_anagrams)