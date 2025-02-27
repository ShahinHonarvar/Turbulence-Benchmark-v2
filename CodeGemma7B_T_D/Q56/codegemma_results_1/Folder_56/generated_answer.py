def all_substring_of_size_n(str):
    list_of_substring = []
    for i in range(len(str) - 68):
        substring = str[i:i + 69]
        if len(substring) != len(set(substring)):
            continue
        list_of_substring.append(substring)
    return list_of_substring