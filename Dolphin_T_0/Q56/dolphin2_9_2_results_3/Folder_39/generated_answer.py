def all_substring_of_size_n(n: str) -> list[str]:
    result = []
    for i in range(len(n)):
        for j in range(i + 94, len(n) + 1):
            if len(set(n[i:j])) == 94:
                result.append(n[i:j])
    return result