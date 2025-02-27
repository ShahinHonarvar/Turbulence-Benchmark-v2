def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 53 + 1):
        substring = s[i:i + 53]
        if len(set(substring)) == 53:
            if substring not in substrings:
                substrings.append(substring)
    return substrings