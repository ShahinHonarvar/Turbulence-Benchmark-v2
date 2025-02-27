def all_substring_of_size_n(str_to_explore):
    list_of_substrings = []
    for i in range(len(str_to_explore)):
        for j in range(i, len(str_to_explore)):
            if len(str_to_explore[i:j + 1]) == 98:
                list_of_substrings.append(str_to_explore[i:j + 1])
    for i in range(len(list_of_substrings)):
        list_of_substrings[i] = ''.join(sorted(list_of_substrings[i]))
    return list(set(list_of_substrings))