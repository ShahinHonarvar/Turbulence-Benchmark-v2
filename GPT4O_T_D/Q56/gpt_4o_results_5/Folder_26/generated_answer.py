def all_substring_of_size_n(s):
    n = 33
    result = []
    seen_substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring not in seen_substrings and len(set(substring)) == n:
            result.append(substring)
            seen_substrings.add(substring)
    return result