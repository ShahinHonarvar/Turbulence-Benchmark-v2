def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 2):
        for j in range(i + 1, len(str) - 1):
            for k in range(j + 1, len(str)):
                substring = str[i:k + 1]
                if len(substring) == len(set(substring)):
                    result.append(substring)
    return result