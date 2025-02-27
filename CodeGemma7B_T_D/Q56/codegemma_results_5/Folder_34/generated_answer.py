def all_substring_of_size_n(str):
    substring_list = []
    for i in range(len(str) - 83):
        substring = str[i:i + 84]
        if substring not in substring_list:
            substring_list.append(substring)
    return substring_list if substring_list else []