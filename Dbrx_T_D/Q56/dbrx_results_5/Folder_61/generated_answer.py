def all_substring_of_size_n(s):
    result = []
    if len(s) < 39 or len(set(s)) != len(s):
        return result
    for i in range(len(s) - 39 + 1):
        substring = s[i:i + 39]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))