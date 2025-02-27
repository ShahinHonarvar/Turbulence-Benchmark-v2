def all_substring_of_size_n(s: str) -> list:
    n = 31
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))