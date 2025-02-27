def all_substring_of_size_n(s):
    if len(s) < 25:
        return []
    result = []
    seen_substrings = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if substring not in seen_substrings and len(set(substring)) == 25:
            result.append(substring)
            seen_substrings.add(substring)
    return result