def all_substring_of_size_n(string):
    if len(string) < 71:
        return []
    distinct_substrings = set()
    for i in range(len(string) - 70):
        substring = string[i:i + 71]
        if len(set(substring)) == 71:
            distinct_substrings.add(substring)
    return list(distinct_substrings)