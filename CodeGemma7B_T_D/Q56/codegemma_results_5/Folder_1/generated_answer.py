def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == len(substring):
            distinct_substrings.add(substring)
    return sorted(list(distinct_substrings))