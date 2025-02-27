def all_substring_of_size_n(string):
    n = 77
    result = []
    for i in range(len(string)):
        for j in range(i + 1, min(i + n + 1, len(string))):
            substring = string[i:j]
            if len(set(substring)) == n:
                result.append(substring)
    return result