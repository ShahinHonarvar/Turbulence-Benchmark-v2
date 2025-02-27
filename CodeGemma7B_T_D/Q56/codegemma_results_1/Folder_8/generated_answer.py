def all_substring_of_size_n(str):
    str2 = set()
    for i in range(len(str) - 29):
        str2.add(str[i:i + 30])
    return list(str2)