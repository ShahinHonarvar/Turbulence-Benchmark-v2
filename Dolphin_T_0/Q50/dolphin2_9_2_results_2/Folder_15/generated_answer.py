def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i]
            str2 = list_of_strings[j]
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1.lower()) == sorted(str2.lower())):
                count += 1
            if count >= 4:
                return True
    return False