def all_substring_of_size_n(s):
    substring_list = []
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98:
            substring_list.append(substring)
    return list(set(substring_list))