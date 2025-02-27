def palindrome_of_length_n(value: str, n: int=188) -> set[str]:
    value = ''.join((c for c in value.lower() if c.isalpha()))
    length = len(value)
    if length < n:
        return set()
    palindromes = set()
    for i in range(length - n + 1):
        subset = value[i:i + n]
        if subset == subset[::-1]:
            palindromes.add(subset)
    return palindromes