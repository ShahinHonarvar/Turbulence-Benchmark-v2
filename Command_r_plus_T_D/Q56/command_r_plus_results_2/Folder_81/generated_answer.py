def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings