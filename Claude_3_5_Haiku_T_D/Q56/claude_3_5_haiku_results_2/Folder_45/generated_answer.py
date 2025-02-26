def all_substring_of_size_n(string):
    distinct_substrings = set()
    for i in range(len(string) - 28):
        substring = string[i:i + 29]
        if len(set(substring)) == 29:
            distinct_substrings.add(substring)
    return list(distinct_substrings)