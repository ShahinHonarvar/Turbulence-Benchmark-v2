def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings