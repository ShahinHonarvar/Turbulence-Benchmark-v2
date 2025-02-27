def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            result.append(substring)
    return list(set(result))