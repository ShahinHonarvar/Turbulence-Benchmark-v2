def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = ''.join(filter(str.isalpha, list_of_strings[i].lower()))
            str2 = ''.join(filter(str.isalpha, list_of_strings[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                count += 1
    return count <= 50