def all_substring_of_size_n(str):
    all_substrings = set()
    for i in range(len(str) - 23):
        substring = str[i:i + 24]
        if len(set(substring)) == 24:
            all_substrings.add(substring)
    return list(all_substrings)