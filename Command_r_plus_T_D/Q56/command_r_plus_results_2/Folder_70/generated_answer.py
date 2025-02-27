def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    length = len(s)
    for i in range(length):
        for j in range(i + 12, length + 1):
            substring = s[i:j]
            if len(substring) == 12 and len(substring) == len(set(substring)):
                result.append(substring)
    return result