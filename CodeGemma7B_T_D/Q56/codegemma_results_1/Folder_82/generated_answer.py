def all_substring_of_size_n(str):
    list1 = []
    for i in range(len(str)):
        for j in range(i + 100, len(str) + 1):
            t = str[i:j]
            if len(t) == len(set(t)):
                list1.append(t)
    return list1