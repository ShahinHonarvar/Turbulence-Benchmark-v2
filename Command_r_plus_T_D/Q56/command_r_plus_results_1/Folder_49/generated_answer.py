def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    for i in range(len(s) - 65):
        substring = s[i:i + 73]
        if len(substring) == 73 and len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings