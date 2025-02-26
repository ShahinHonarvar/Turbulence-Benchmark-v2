def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        if len(set(substring)) == 124:
            distinct_substrings.add(substring)
    return list(distinct_substrings)