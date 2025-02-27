def palindromes_of_specific_lengths(s: str) -> set:
    s = s[75:96]
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1]:
                if all((char.isalpha() for char in substring)):
                    palindromes.add(substring)
    return palindromes