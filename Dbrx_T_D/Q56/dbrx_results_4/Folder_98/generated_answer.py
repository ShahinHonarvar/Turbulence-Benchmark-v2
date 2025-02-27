def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 10 + 1):
        substring = s[i:i + 10]
        if len(set(substring)) == 10:
            result.append(substring)
    return list(set(result))