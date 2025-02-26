def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if len(set(substring)) == 78:
            distinct_substrings.add(substring)
    return list(distinct_substrings)