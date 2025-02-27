def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(set(substring)) == 28:
            substrings.append(substring)
    return substrings