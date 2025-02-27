def all_substring_of_size_n(s):
    length = 99
    result = []
    if len(s) < length:
        return result
    seen_substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length and substring not in seen_substrings:
            seen_substrings.add(substring)
    return list(seen_substrings)