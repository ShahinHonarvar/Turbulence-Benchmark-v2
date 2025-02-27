def all_substring_of_size_n(str):
    unique_substrings = set()
    for i in range(len(str) - 145):
        substring = str[i:i + 146]
        if len(set(substring)) == 146:
            unique_substrings.add(substring)
    return list(unique_substrings)