def all_substring_of_size_n(s):
    substr_list = []
    for i in range(len(s) - 39):
        sub = s[i:i + 40]
        if len(set(sub)) == 40:
            substr_list.append(sub)
    return list(set(substr_list))