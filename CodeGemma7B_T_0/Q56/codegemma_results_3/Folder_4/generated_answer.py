def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if len(set(str[i:j + 1])) == 41:
                result.add(str[i:j + 1])
    return list(result)