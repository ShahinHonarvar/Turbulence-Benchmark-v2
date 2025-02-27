def all_substring_of_size_n(str):
    list = []
    for i in range(len(str) - 73):
        for j in range(i + 1, len(str) - 72 + i):
            substring = str[i:j + 1]
            if len(substring) == len(set(substring)):
                list.append(substring)
    if len(list) == 0:
        return []
    return list