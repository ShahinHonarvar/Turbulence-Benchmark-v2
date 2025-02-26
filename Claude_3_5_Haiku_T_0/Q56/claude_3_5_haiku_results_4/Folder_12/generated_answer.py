def all_substring_of_size_n(s):
    if len(s) < 47:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if len(set(substring)) == 47:
            distinct_substrings.add(substring)
    return list(distinct_substrings)