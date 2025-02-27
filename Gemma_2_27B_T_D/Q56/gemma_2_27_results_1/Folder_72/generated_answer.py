def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 87):
        substring = s[i:i + 88]
        if len(set(substring)) == 88:
            result.append(substring)
    return result