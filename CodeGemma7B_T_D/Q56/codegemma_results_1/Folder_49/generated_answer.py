def all_substring_of_size_n(str1):
    list1 = []
    for i in range(len(str1) - 72):
        for j in range(i + 1, len(str1)):
            str2 = str1[i:j + 1]
            if len(set(str2)) == 73:
                list1.append(str2)
    return list1