def all_substring_of_size_n(s):
    result = []
    length = 110
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            result.append(substring)
    return result