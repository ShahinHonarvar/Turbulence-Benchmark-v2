def palindromes_of_specific_lengths(s: str) -> set:
    s = s[22:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes