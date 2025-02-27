def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) and len(substring) == 46
    valid_substrings = []
    string_length = len(s)
    for i in range(string_length):
        for j in range(i + 1, string_length + 1):
            substring = s[i:j]
            if len(substring) == 46 and is_substring_valid(substring):
                valid_substrings.append(substring)
    return valid_substrings