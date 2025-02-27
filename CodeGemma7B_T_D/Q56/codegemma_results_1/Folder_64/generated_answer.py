def all_substring_of_size_n(str_arg):
    substrings = set()
    for i in range(len(str_arg) - 7):
        substring = str_arg[i:i + 8]
        substrings.add(substring)
    return list(substrings)