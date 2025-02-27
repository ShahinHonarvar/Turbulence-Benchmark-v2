def palindrome_of_length_at_least_n(text: str, n: int=19) -> set:
    if n < 0:
        raise ValueError('The length of the palindrome should be non-negative.')
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes