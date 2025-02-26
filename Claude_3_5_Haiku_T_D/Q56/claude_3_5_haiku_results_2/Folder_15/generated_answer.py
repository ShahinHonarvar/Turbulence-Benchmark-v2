def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            unique_substrings.add(substring)
    return list(unique_substrings)