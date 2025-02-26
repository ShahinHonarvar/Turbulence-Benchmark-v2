def all_substring_of_size_n(s):
    if len(s) < 33:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 32):
        substring = s[i:i + 33]
        if len(set(substring)) == 33:
            distinct_substrings.add(substring)
    return list(distinct_substrings)