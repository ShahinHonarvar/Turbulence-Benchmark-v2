def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14 and len(substring) == 14:
            result.append(substring)
    return list(set(result))