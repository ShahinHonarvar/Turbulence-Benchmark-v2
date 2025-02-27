def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings