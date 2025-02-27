def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            str1 = ''.join(sorted(string_list[i].lower()))
            str2 = ''.join(sorted(string_list[j].lower()))
            if str1 == str2 and len(str1) >= 3:
                count += 1
    return count <= 289