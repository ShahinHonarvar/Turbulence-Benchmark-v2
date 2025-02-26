def all_substring_of_size_n(s):
    if len(s) < 77:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if len(set(substring)) == 77:
            distinct_substrings.add(substring)
    return list(distinct_substrings)