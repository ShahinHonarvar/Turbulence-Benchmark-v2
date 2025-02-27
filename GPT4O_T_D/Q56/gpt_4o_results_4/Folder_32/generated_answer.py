def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 70):
        substring = s[i:i + 71]
        if len(substring) == 71 and len(set(substring)) == 71:
            result.append(substring)
    return result