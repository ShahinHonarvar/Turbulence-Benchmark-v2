def all_substring_of_size_n(s):
    if len(s) < 90:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90:
            distinct_substrings.add(substring)
    return list(distinct_substrings)