def all_substring_of_size_n(str):
    a = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if len(substring) == 75 and len(set(substring)) == len(substring):
                a.add(substring)
    return list(a)