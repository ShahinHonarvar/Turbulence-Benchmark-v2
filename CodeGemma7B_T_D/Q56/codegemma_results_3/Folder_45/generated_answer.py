def all_substring_of_size_n(str):
    str_len = len(str)
    result = set()
    for i in range(str_len - 28):
        j = i + 29
        substring = str[i:j]
        if len(set(substring)) == 29:
            result.add(substring)
    return list(result)