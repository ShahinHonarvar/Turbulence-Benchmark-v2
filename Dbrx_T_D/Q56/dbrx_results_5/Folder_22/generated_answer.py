def all_substring_of_size_n(s):
    result = []
    if len(s) < 22:
        return result
    for i in range(0, len(s) - 21):
        substring = s[i:i + 22]
        if len(substring) == 22 and len(set(substring)) == 22:
            result.append(substring)
    return list(set(result))