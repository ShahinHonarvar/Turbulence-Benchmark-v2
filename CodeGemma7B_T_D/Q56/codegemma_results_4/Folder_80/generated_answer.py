def all_substring_of_size_n(str):
    list = []
    for i in range(0, len(str)):
        for j in range(0, len(str)):
            if j - i + 1 == 31 and len(set(str[i:j + 1])) == 31:
                list.append(str[i:j + 1])
    return list