def all_substring_of_size_n(string):
    result = set()
    n = 100
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)