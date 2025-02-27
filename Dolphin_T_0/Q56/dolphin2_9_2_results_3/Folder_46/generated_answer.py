def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    substring_list = []
    for i in range(0, len(s) - 86):
        substring = s[i:i + 87]
        if len(set(substring)) == 87:
            substring_list.append(substring)
    return substring_list