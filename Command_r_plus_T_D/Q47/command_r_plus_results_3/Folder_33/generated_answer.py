def palindromes_of_specific_lengths(s: str) -> set:
    s = s[130:296]
    s = s.lower()
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes