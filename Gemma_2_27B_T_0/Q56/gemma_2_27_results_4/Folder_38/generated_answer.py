def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 34):
        substring = s[i:i + 35]
        if len(set(substring)) == 35:
            result.append(substring)
    return result