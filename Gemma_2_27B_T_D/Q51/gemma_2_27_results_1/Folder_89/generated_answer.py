def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            str1 = string_list[i].lower()
            str2 = string_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    count += 1
    return count <= 73