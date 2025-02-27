def all_substring_of_size_n(s):
    substr_list = []
    for i in range(len(s) - 9):
        sub = s[i:i + 9]
        if len(set(sub)) == 9:
            if sub not in substr_list:
                substr_list.append(sub)
    return substr_list