def palindromes_between_indices(text: str) -> set[str]:
    if len(text[7:10]) < 3:
        return set()
    words = [''] * (len(text[7:10]) + 1)
    for i, char in enumerate(text[7:10]):
        words[i + 1] = words[i] + char
        words[len(text[7:10]) - i - 1] = words[i] + words[len(text[7:10]) - i - 1]
    return set((''.join(p) for p in words if p[0] <= p[-1]))