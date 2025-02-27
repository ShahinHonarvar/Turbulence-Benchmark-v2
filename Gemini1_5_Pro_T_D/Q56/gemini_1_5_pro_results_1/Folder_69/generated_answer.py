def all_substring_of_size_n(s: str) -> list[str]:
    substrings = []
    if len(s) >= 99:
        for i in range(len(s) - 98):
            substring = s[i:i + 99]
            if len(set(substring)) == 99 and substring not in substrings:
                substrings.append(substring)
    return substrings