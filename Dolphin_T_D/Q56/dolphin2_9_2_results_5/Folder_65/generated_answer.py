def all_substring_of_size_n(string):
    if len(string) < 81:
        return []
    substring_list = []
    for i in range(len(string) - 80):
        substring = string[i:i + 81]
        if len(set(substring)) == len(substring):
            substring_list.append(substring)
    return substring_list