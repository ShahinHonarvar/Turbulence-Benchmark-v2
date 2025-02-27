def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s) - 44):
        substring = s[i:i + 45]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings