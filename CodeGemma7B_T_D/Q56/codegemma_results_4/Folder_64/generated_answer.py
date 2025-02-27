def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 7):
        cur = str[i:i + 8]
        if len(set(cur)) == 8:
            result.add(cur)
    return list(result)