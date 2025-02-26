def all_substring_of_size_n(s):
    if len(s) < 68:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            distinct_substrings.add(substring)
    return list(distinct_substrings)