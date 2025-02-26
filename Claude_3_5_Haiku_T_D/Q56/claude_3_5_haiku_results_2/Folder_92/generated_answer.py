def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 8):
        substring = s[i:i + 9]
        if len(set(substring)) == 9:
            distinct_substrings.add(substring)
    return list(distinct_substrings)