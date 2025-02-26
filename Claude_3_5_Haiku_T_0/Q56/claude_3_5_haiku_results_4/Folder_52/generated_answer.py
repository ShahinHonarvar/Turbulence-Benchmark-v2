def all_substring_of_size_n(s):
    if len(s) < 15:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 14):
        substring = s[i:i + 15]
        if len(set(substring)) == 15:
            distinct_substrings.add(substring)
    return list(distinct_substrings)