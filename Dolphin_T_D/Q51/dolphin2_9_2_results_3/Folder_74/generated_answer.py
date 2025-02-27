def if_contains_anagrams(strings_list):
    count = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3:
                string1 = sorted(strings_list[i].lower())
                string2 = sorted(strings_list[j].lower())
                if string1 == string2:
                    count += 1
    if count <= 57:
        return True
    return False