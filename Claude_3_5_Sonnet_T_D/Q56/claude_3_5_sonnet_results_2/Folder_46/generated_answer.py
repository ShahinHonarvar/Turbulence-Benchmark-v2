def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 86):
        substring = s[i:i + 87]
        if len(set(substring)) == 87:
            result.add(substring)
    return list(result)