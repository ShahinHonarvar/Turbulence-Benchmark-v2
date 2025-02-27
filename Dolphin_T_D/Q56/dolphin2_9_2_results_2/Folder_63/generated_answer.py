def all_substring_of_size_n(s: str) -> list:
    n = 19
    substrings = set()
    if len(s) < n:
        return []
    else:
        for i in range(len(s) - n + 1):
            substring = s[i:i + n]
            if len(set(substring)) == n:
                substrings.add(''.join(sorted(substring)))
    return [list(map(int, [*s])) for s in substrings]