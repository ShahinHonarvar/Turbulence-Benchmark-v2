def all_substring_of_size_n(s):
    unique_substrings = set()
    for i in range(len(s) - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            unique_substrings.add(substring)
    return list(unique_substrings)