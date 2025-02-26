def all_substring_of_size_n(s):
    if len(s) < 20:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20:
            distinct_substrings.add(substring)
    return list(distinct_substrings)