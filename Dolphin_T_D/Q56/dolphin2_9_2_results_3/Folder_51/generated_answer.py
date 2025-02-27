def all_substring_of_size_n(s):
    substr_list = []
    for i in range(len(s) - 96 + 1):
        substring = s[i:i + 96]
        if len(set(list(substring))) == 96:
            substr_list.append(substring)
    return list(set(substr_list))