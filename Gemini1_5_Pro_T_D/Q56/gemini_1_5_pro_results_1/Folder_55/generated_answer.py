def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) >= 40:
        for i in range(len(s) - 39):
            substring = s[i:i + 40]
            if len(set(substring)) == 40:
                substrings.append(substring)
    return substrings