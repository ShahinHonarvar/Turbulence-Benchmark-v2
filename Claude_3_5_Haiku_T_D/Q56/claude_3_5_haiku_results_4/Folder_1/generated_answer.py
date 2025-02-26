def all_substring_of_size_n(string):
    if len(string) < 24:
        return []
    distinct_substrings = set()
    for i in range(len(string) - 23):
        substring = string[i:i + 24]
        if len(set(substring)) == 24:
            distinct_substrings.add(substring)
    return list(distinct_substrings)