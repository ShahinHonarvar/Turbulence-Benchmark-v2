def all_substring_of_size_n(s):
    if len(s) < 40:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            distinct_substrings.add(substring)
    return list(distinct_substrings)