def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            distinct_substrings.add(substring)
    return list(distinct_substrings)