def all_substring_of_size_n(mystring):
    substring_list = []
    for i in range(len(mystring)):
        for j in range(i + 1, len(mystring)):
            if j - i + 1 == 110:
                if mystring[i:j + 1] not in substring_list:
                    substring_list.append(mystring[i:j + 1])
    return substring_list