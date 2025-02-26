def all_substring_of_size_n(s):
    if len(s) < 38:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            distinct_substrings.add(substring)
    return list(distinct_substrings)