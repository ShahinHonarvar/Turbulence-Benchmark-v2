def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result