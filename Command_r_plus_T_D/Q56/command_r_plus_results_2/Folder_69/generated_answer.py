def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings = [s[i:i + 99] for i in range(len(s) - 98)]
    valid_substrings = [sub for sub in substrings if is_substring_valid(sub)]
    return valid_substrings