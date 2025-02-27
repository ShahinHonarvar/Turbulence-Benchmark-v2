def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6:
            result.append(substring)
    return list(set(result))