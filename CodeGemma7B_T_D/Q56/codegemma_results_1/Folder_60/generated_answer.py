def all_substring_of_size_n(arg):
    substrings = set()
    for i in range(len(arg) - 35):
        substring = arg[i:i + 36]
        substrings.add(substring)
    return list(substrings)