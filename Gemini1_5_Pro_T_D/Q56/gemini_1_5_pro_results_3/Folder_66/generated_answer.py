def all_substring_of_size_n(s):
    substrings = []
    seen_substring = set()
    n = 26
    if len(s) < n:
        return substrings
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen_substring:
            substrings.append(substring)
            seen_substring.add(substring)
    return substrings