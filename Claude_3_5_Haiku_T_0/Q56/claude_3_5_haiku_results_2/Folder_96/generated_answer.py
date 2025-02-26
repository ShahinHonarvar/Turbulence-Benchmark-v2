def all_substring_of_size_n(s):
    if len(s) < 21:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21:
            distinct_substrings.add(substring)
    return list(distinct_substrings)