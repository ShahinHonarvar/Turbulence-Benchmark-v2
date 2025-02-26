def all_substring_of_size_n(s):
    if len(s) < 34:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(set(substring)) == 34:
            distinct_substrings.add(substring)
    return list(distinct_substrings)