def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings