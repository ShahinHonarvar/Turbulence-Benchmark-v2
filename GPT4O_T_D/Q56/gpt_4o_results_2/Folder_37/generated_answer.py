def all_substring_of_size_n(s):
    n = 65
    result = []
    seen_substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen_substrings:
            seen_substrings.add(substring)
            result.append(substring)
    return result