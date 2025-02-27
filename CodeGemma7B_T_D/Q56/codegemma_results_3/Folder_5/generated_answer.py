def all_substring_of_size_n(str):
    if len(str) <= 64:
        return []
    list_of_substrings = []
    for i in range(len(str) - 64 + 1):
        substring = str[i:i + 64]
        if substring in list_of_substrings:
            continue
        list_of_substrings.append(substring)
    return list_of_substrings