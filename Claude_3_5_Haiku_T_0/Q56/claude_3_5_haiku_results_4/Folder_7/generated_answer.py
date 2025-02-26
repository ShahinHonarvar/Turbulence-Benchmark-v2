def all_substring_of_size_n(s):
    if len(s) < 117:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 116):
        substring = s[i:i + 117]
        if len(set(substring)) == 117:
            distinct_substrings.add(substring)
    return list(distinct_substrings)