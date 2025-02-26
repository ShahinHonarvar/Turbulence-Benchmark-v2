def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 53):
        substr = s[i:i + 54]
        if len(set(substr)) == 54:
            distinct_substrings.add(substr)
    return list(distinct_substrings)