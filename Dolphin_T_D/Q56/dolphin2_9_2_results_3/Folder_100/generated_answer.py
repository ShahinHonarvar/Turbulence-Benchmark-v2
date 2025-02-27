def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 8):
        substring = s[i:i + 9]
        if len(set(substring)) == 9:
            result.append(subsring)
    return result