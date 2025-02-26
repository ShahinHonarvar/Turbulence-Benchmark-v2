def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if len(set(substring)) == 96:
            distinct_substrings.add(substring)
    return list(distinct_substrings)