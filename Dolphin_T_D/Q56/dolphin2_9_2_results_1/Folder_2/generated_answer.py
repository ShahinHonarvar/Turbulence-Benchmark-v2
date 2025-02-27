def all_substring_of_size_n(string):
    n = 56
    result = []
    for i in range(len(string) - n + 1):
        sub = string[i:i + n]
        if len(set(sub)) == n:
            result.append(sub)
    return result