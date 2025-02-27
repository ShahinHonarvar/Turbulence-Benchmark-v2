def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result