def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if len(set(substring)) == 81:
            distinct_substrings.add(substring)
    return list(distinct_substrings)