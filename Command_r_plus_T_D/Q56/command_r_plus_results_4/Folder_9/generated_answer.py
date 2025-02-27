def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result