def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 99 and len(set(substring)) == 99
    valid_substrings = []
    string_length = len(s)
    for i in range(string_length - 98):
        substring = s[i:i + 99]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings