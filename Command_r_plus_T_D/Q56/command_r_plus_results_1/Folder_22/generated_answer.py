def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    result = []
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if is_substring_valid(substring):
            result.append(substring)
    return result