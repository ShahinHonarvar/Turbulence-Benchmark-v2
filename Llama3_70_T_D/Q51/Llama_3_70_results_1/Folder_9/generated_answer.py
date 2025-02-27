def if_contains_anagrams(list_strings):
    anagrams_count = 0
    for i in range(len(list_strings)):
        for j in range(i + 1, len(list_strings)):
            string1 = ''.join(filter(str.isalpha, list_strings[i].lower()))
            string2 = ''.join(filter(str.isalpha, list_strings[j].lower()))
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1) == sorted(string2)):
                anagrams_count += 1
    return anagrams_count <= 475