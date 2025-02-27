def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 15, length + 1):
            substring = s[i:j]
            if len(substring) == 15 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings