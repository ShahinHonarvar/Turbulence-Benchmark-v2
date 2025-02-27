def palindromes_of_specific_lengths(text: str) -> set:
    text = text.lower()
    palindromes = set()
    for length in range(10, 51):
        for start in range(200, 301 - length):
            substring = text[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes