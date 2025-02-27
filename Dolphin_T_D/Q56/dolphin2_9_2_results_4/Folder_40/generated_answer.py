def all_substring_of_size_n(s):
    existing_substrings = set()
    for i in range(len(s) - 1):
        substr = s[i:i + 2]
        if len(set(substr)) == len(substr):
            existing_substrings.add(substr)
    return list(existing_substrings)