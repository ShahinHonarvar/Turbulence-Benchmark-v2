def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if len(set(substring)) == 96:
            result.append(substring)
    return result