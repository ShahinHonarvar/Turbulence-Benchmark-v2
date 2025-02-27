def all_substring_of_size_n(str):
    result = []
    for i in range(len(str)):
        for j in range(i, len(str)):
            substring = str[i:j + 1]
            if len(substring) == 10 and len(set(substring)) == 10:
                result.append(substring)
    return result