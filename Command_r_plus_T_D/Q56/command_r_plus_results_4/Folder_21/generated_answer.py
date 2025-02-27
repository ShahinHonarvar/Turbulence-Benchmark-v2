def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 106
    substrings = []
    length_s = len(s)
    for i in range(length_s):
        for j in range(i + 1, length_s + 1):
            substring = s[i:j]
            if len(substring) == 106 and is_substring_valid(substring):
                substrings.append(substring)
    return substrings