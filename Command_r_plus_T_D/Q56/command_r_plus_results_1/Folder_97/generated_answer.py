def all_substring_of_size_n(s: str) -> list[str]:

    def is_substring_valid(sub: str) -> bool:
        return len(sub) == 142 and len(set(sub)) == 142
    substrings = []
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings