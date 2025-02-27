def all_substring_of_size_n(s: str) -> list[str]:

    def is_valid_substring(substring):
        return len(substring) == 93 and len(substring) == len(set(substring))
    substrings = []
    for i in range(len(s)):
        for j in range(i + 93, len(s) + 1):
            substring = s[i:j]
            if is_valid_substring(substring):
                substrings.append(substring)
    return substrings