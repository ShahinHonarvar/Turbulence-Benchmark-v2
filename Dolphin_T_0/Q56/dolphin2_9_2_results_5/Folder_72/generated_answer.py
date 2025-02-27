def all_substring_of_size_n(str):
    if len(set(str)) != len(str):
        return []
    n = len(str)
    s = set()
    if n < 88:
        return []
    for i in range(n - 87):
        temp = str[i:i + 88]
        if len(set(temp)) == 88:
            s.add(temp)
    return list(s)