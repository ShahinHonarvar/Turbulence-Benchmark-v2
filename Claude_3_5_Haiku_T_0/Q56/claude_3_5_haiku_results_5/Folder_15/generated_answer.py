def all_substring_of_size_n(s):
    if len(s) < 3:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            distinct_substrings.add(substring)
    return list(distinct_substrings)