def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 32
    substrings = []
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings