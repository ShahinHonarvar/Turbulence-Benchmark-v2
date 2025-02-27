def all_substring_of_size_n(str):
    n = 37
    result = []
    for i in range(len(str) - (n - 1)):
        substring = str[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result