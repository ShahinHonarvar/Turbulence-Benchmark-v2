def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            result.append(substring)
    return result