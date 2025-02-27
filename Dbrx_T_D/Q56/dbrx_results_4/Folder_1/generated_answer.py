def all_substring_of_size_n(string):
    result = set()
    n = 24
    if n > len(string):
        return []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            result.add(substring)
    return list(result)