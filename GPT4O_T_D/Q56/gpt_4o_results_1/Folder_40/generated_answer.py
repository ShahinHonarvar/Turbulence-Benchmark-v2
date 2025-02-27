def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 1):
        substring = s[i:i + 2]
        if len(set(substring)) == 2:
            result.append(substring)
    return list(set(result))