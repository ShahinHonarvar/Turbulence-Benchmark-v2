def all_substring_of_size_n(string):
    if len(string) < 56:
        return []
    distinct_substrings = set()
    for i in range(len(string) - 55):
        substring = string[i:i + 56]
        if len(set(substring)) == 56:
            distinct_substrings.add(substring)
    return list(distinct_substrings)