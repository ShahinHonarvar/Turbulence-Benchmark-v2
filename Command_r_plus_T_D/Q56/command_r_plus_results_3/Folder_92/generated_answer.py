def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    length = len(s)
    for i in range(length):
        for j in range(i + 9, length + 1):
            substring = s[i:j]
            if len(substring) == 9 and len(set(substring)) == 9:
                result.append(substring)
    return result