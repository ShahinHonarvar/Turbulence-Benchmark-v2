def all_substring_of_size_n(s):
    if len(s) < 31:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 30):
        substring = s[i:i + 31]
        if len(set(substring)) == 31:
            distinct_substrings.add(substring)
    return list(distinct_substrings)