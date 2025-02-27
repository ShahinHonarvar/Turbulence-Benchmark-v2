def all_substring_of_size_n(s):
    substr_list = []
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(set(substring)) == len(substring) and len(substring) == 127:
            substr_list.append(substring)
    return list(set(substr_list))