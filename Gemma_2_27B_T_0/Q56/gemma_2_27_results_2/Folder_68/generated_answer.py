def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 74):
        substring = s[i:i + 75]
        if len(set(substring)) == 75:
            result.append(substring)
    return result