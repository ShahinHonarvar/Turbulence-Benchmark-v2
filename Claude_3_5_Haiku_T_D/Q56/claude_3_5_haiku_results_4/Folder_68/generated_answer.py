def all_substring_of_size_n(string):
    if len(string) < 75:
        return []
    distinct_substrings = set()
    for i in range(len(string) - 74):
        substring = string[i:i + 75]
        if len(set(substring)) == 75:
            distinct_substrings.add(substring)
    return list(distinct_substrings)