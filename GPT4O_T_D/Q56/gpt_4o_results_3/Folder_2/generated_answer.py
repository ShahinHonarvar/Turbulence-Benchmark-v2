def all_substring_of_size_n(s):
    result = []
    size = 56
    if len(s) < size:
        return result
    for i in range(len(s) - size + 1):
        substring = s[i:i + size]
        if len(set(substring)) == size and len(substring) == size:
            result.append(substring)
    return list(set(result))