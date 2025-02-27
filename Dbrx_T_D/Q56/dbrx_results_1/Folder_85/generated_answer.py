def all_substring_of_size_n(s: str) -> list:
    substrings = []
    if len(s) < 14:
        return substrings
    for i in range(len(s) - 13):
        substring = ''.join(sorted(s[i:i + 14]))
        if substring not in substrings:
            substrings.append(substring)
    return substrings