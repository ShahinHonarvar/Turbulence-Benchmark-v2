def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    substring_list = []
    for i in range(len(s) - 11 + 1):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            substring_list.append(substring)
    return substring_list