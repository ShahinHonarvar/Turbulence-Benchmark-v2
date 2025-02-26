def all_substring_of_size_n(s):
    if len(s) < 94:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 93):
        substr = s[i:i + 94]
        if len(set(substr)) == 94:
            distinct_substrings.add(substr)
    return list(distinct_substrings)