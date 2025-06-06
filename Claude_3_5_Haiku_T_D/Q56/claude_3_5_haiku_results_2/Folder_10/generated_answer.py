def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 54):
        substring = s[i:i + 55]
        if len(set(substring)) == 55:
            distinct_substrings.add(substring)
    return list(distinct_substrings)