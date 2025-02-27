def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) < 3 or len(str2) < 3:
                continue
            str1_sorted = ''.join(sorted(str1))
            str2_sorted = ''.join(sorted(str2))
            if str1_sorted == str2_sorted:
                count += 1
    return count >= 78