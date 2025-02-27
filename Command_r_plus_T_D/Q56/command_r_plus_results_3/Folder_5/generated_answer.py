def all_substring_of_size_n(s: str) -> list[str]:

    def is_valid_substring(substring: str) -> bool:
        return len(substring) == 64 and len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s) - 63):
        substring = s[i:i + 64]
        if is_valid_substring(substring):
            substrings.append(substring)
    return substrings