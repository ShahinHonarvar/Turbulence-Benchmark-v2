def all_substring_of_size_n(str):
    str = str.lower()
    size = 149
    list = []
    for i in range(len(str)):
        for j in range(i + size):
            if j - i == size:
                temp = str[i:j]
                if not temp in list:
                    list.append(temp)
    return list