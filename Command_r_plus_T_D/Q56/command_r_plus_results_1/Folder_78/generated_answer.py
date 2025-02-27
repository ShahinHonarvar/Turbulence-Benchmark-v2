def all_substring_of_size_n(s: str) -> list[str]:

    def is_valid_substring(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s) - 48):
        substring = s[i:i + 49]
        if is_valid_substring(substring):
            substrings.append(substring)
    return substrings