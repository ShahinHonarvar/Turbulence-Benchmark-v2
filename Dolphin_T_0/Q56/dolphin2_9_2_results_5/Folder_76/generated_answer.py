def all_substring_of_size_n(string):
    substr_list = []
    for i in range(len(string) - 148):
        if len(set(string[i:i + 149])) == 149:
            substr_list.append(string[i:i + 149])
    return list(set(substr_list))