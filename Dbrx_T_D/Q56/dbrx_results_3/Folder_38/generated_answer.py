def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 35 + 1):
        substring = s[i:i + 35]
        if len(substring) == 35 and len(set(substring)) == 35:
            result.append(substring)
    return list(set(result))