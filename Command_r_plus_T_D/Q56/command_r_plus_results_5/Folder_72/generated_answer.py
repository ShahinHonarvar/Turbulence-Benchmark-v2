def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s)):
        for j in range(i + 88, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 88 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings