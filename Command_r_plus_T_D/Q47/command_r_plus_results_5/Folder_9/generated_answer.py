def palindromes_of_specific_lengths(s: str) -> set:
    s = s[:301].lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(11):
            substring = s[i:i + 50 + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes