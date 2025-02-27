def all_substring_of_size_n(str):
    unique_substrings = set()
    for i in range(len(str) - 39):
        substring = str[i:i + 40]
        unique_substrings.add(substring)
    return list(unique_substrings)