def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for i in range(len(strings_list) - 1):
        for j in range(i + 1, len(strings_list)):
            string1 = strings_list[i].lower()
            string2 = strings_list[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1) == sorted(string2)):
                anagrams_count += 1
    return anagrams_count <= 423