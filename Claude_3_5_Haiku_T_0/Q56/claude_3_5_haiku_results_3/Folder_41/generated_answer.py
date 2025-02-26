def all_substring_of_size_n(s):
    if len(s) < 74:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 73):
        substring = s[i:i + 74]
        if len(set(substring)) == 74:
            distinct_substrings.add(substring)
    return list(distinct_substrings)