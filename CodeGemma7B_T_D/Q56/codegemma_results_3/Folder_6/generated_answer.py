def all_substring_of_size_n(str):
    list_of_substr = []
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if len(set(str[i:j + 1])) > 22:
                continue
            list_of_substr.append(str[i:j + 1])
    return list_of_substr