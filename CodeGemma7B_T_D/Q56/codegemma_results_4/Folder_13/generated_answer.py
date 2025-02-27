def all_substring_of_size_n(string):
    if len(string) != 53:
        return []
    substring_list = []
    for i in range(len(string) - 4):
        substring = string[i:i + 53]
        if substring not in substring_list:
            substring_list.append(substring)
    return substring_list