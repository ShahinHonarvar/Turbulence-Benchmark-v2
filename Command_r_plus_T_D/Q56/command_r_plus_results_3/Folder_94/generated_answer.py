def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 70
    valid_substrings = []
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings