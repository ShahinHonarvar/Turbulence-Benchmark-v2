def all_substring_of_size_n(str):
    result = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substring = str[i:j]
            if len(substring) == 2 and substring not in result:
                result.append(substring)
    return result