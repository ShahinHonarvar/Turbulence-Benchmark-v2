def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            distinct_substrings.add(substring)
    return list(distinct_substrings)