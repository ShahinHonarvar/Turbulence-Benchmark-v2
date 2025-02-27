def all_substring_of_size_n(str):
    list_size_n = []
    for i in range(len(str)):
        if i + 81 < len(str) + 1:
            tmp = str[i:i + 81]
            if len(tmp) == len(set(tmp)):
                list_size_n.append(tmp)
    return list_size_n