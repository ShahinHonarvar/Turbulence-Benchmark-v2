def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            distinct_substrings.add(substring)
    return list(distinct_substrings)