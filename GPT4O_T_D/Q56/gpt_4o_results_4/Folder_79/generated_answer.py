def all_substring_of_size_n(s):
    result = []
    length = len(s)
    if length < 61:
        return result
    for i in range(length - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            result.append(substring)
    return result