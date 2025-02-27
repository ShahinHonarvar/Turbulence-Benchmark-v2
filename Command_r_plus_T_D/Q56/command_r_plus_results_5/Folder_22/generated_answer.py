def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings