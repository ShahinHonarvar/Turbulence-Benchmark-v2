def all_substring_of_size_n(str):
    L = len(str)
    for i in range(L):
        for j in range(i + 54, L + 1):
            substring = str[i:j]
            if len(substring) == 54 and len(set(substring)) == 54:
                return [substring]
    return []