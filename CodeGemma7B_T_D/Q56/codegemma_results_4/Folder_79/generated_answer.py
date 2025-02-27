def all_substring_of_size_n(text: str) -> list[str]:
    result = set()
    for start in range(len(text) - 61 + 1):
        for end in range(start + 61, len(text) + 1):
            substring = text[start:end]
            if len(set(substring)) == 61:
                result.add(substring)
    return list(result)