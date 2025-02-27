def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    for length in range(5, 11):
        for i in range(100, 201 - length):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes