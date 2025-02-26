def all_substring_of_size_n(s):
    if len(s) < 54:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 53):
        substring = s[i:i + 54]
        if len(set(substring)) == 54:
            distinct_substrings.add(substring)
    return list(distinct_substrings)