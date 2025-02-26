def all_substring_of_size_n(s):
    if len(s) < 42:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if len(set(substring)) == 42:
            distinct_substrings.add(substring)
    return list(distinct_substrings)