def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    result = set()
    for i in range(len(s) - 88):
        temp = s[i:i + 89]
        if len(set(temp)) == len(temp):
            result.add(temp)
    return list(result)