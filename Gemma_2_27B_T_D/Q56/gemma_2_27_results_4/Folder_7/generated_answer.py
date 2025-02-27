def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 116):
        substring = s[i:i + 117]
        if len(set(substring)) == 117:
            result.append(substring)
    return result