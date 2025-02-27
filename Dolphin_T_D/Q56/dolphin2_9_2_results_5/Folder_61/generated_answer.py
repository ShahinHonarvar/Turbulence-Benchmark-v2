def all_substring_of_size_n(string):
    if len(string) < 39:
        return []
    result = set()
    for i in range(len(string) - 38):
        temp = string[i:i + 39]
        if len(set(temp)) == 39:
            result.add(temp)
    return list(result)