def all_substring_of_size_n(s):
    if len(s) < 61:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            distinct_substrings.add(substring)
    return list(distinct_substrings)