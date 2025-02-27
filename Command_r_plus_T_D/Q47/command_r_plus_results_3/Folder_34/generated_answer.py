def palindromes_of_specific_lengths(text: str) -> set:
    palindromes = set()
    substring = text[200:301].lower()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes