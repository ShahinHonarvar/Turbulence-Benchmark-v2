def all_substring_of_size_n(str):
    all_unique = set()
    for i in range(len(str) - 95 + 1):
        for j in range(i, len(str)):
            substring = str[i:j + 1]
            if len(substring) == len(set(substring)):
                all_unique.add(substring)
    return list(all_unique)