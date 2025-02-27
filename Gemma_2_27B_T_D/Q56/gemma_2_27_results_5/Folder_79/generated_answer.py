def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            result.append(substring)
    return result