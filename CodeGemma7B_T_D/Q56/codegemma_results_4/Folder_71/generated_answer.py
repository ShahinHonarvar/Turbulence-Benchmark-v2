def all_substring_of_size_n(text):
    if len(text) < 17:
        return []
    distinct_substrings = set()
    for i in range(len(text) - 16):
        substring = text[i:i + 17]
        if len(set(substring)) == 17:
            distinct_substrings.add(substring)
    return list(distinct_substrings)