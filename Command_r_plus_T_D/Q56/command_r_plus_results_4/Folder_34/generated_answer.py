def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    n = 84
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings