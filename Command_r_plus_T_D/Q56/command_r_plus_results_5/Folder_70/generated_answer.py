def all_substring_of_size_n(s: str) -> list[str]:
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i == 12 and len(set(s[i:j])) == 12:
                result.append(s[i:j])
    return result