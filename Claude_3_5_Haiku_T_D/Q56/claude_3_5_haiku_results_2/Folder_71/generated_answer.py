def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 16):
        substring = s[i:i + 17]
        if len(set(substring)) == 17:
            distinct_substrings.add(substring)
    return list(distinct_substrings)