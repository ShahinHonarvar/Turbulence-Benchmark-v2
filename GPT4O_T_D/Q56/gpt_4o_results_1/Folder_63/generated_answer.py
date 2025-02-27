def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            unique_substrings.add(substring)
    return list(unique_substrings)