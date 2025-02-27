def all_substring_of_size_n(s):
    length = len(s)
    result = []
    for i in range(length):
        for j in range(i + 75, length + 1):
            substring = s[i:j]
            if len(set(substring)) == len(substring) and len(substring) == 75:
                result.append(substring)
    return result