def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 98 and len(set(substring)) == 98
    valid_substrings = []
    string_length = len(s)
    for i in range(string_length):
        for j in range(i + 98, string_length + 1):
            substring = s[i:j]
            if is_substring_valid(substring):
                valid_substrings.append(substring)
    return valid_substrings