def all_substring_of_size_n(s):
    if len(s) < 10:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if len(set(substring)) == 10:
            distinct_substrings.add(substring)
    return list(distinct_substrings)