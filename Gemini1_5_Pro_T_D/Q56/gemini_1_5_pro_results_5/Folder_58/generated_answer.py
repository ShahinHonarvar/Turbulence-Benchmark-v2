def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) < 127:
        return substrings
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(set(substring)) == 127:
            substrings.append(substring)
    return list(set(substrings))