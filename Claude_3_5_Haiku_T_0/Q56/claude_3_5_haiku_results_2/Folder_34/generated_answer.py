def all_substring_of_size_n(s):
    if len(s) < 84:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if len(set(substring)) == 84:
            distinct_substrings.add(substring)
    return list(distinct_substrings)