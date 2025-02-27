def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(sub: str) -> bool:
        return len(sub) == len(set(sub))
    substrings = []
    for i in range(len(s) - 66):
        substring = s[i:i + 67]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings