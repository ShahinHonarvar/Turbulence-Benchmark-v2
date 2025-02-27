def all_substring_of_size_n(string):
    n = 5
    result = []
    for i in range(len(string)):
        if len(set(string[i:i + n])) == n and len(string) - i + 1 >= n:
            result.append(string[i:i + n])
    return result