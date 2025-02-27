def filter_chars(str):
    for i in range(1, 7):
        c = str[i]
        for j in range(len(str)):
            if str[j] == c and j != i:
                str = str[:j] + str[j + 1:]
    return str