def palindromes_of_specific_lengths(text: str) -> set[str]:
    text = text.lower()
    palindromes = set()
    for i in range(11, 84):
        for length in range(13, 67):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes