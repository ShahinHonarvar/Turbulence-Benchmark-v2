def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 1):
        substring = s[i:i + 2]
        if len(substring) == 2 and substring[0] != substring[1]:
            result.append(substring)
    return list(set(result))