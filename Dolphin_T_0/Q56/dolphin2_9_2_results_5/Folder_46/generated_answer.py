def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 86):
        substring = s[i:i + 87]
        if len(set(substring)) == 87:
            result.append(substring)
    return list(set(result))