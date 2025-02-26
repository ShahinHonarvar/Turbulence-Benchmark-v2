def all_substring_of_size_n(s):
    if len(s) < 143:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            distinct_substrings.add(substring)
    return list(distinct_substrings)