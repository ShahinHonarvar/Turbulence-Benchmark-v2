def all_substring_of_size_n(s):
    result = []
    length = len(s)
    if length < 68:
        return result
    for i in range(length - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            result.append(substring)
    return result