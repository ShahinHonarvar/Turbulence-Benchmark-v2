def palindromes_of_specific_lengths(text: str) -> set:
    palindromes = set()
    substring = text[69:141].lower()
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes