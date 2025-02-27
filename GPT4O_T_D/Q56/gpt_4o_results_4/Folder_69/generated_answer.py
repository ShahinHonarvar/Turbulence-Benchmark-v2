def all_substring_of_size_n(s):
    if len(s) < 99:
        return []
    substrings = set()
    seen_substrings = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if substring not in seen_substrings and len(set(substring)) == 99:
            substrings.add(substring)
        seen_substrings.add(substring)
    return list(substrings)