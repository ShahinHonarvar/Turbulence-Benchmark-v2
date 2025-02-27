def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    n = 105
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            if substring not in result:
                result.append(substring)
    return result