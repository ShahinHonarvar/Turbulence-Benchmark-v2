def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if len(set(sub)) == 71:
                result.append(sub)
    return result