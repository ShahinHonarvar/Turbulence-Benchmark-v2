def all_substring_of_size_n(string):
    result = []
    n = 49
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            if substring not in result:
                result.append(substring)
    return result