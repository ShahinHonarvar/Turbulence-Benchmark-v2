def all_substring_of_size_n(s):
    distinct_substrings = set()
    for i in range(len(s) - 63):
        substring = s[i:i + 64]
        if len(set(substring)) == 64:
            distinct_substrings.add(substring)
    return list(distinct_substrings)