def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring):
        return len(substring) == len(set(substring)) == 96
    valid_substrings = []
    string_length = len(s)
    for i in range(string_length - 95):
        substring = s[i:i + 96]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings