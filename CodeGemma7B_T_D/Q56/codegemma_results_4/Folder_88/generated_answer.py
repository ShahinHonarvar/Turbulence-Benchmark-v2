def all_substring_of_size_n(str):
    list = []
    for i in range(len(str) - 67):
        substr = str[i:i + 68]
        if substr not in list:
            list.append(substr)
    return list