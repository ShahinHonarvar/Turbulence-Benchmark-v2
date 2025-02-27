def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    length = len(s)
    for i in range(length - 45):
        substring = s[i:i + 46]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result