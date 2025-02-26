def all_substring_of_size_n(s):
    if len(s) < 91:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91:
            distinct_substrings.add(substring)
    return list(distinct_substrings)