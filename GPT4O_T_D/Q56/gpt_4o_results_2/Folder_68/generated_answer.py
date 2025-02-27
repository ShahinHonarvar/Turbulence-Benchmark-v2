def all_substring_of_size_n(s):
    n = len(s)
    if n < 75:
        return []
    result = []
    seen_substrings = set()
    for i in range(n - 74):
        substring = s[i:i + 75]
        if substring not in seen_substrings and len(set(substring)) == 75:
            result.append(substring)
            seen_substrings.add(substring)
    return result