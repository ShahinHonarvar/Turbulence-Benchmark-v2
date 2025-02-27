def all_substring_of_size_n(string):
    substring_list = []
    for i in range(len(string) - 32):
        substring_list.append(string[i:i + 33])
    return list(set(substring_list))