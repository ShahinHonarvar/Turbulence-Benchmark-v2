def all_substring_of_size_n(str):
    if len(set(str)) != len(str):
        return []
    result = []
    for i in range(len(str) - 60):
        temp = str[i:i + 61]
        if not any((i == j for i in temp[:-1] for j in temp[1:])):
            result.append(temp)
    return result