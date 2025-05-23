def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[:301].lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(50, 61):
            if i + j > len(s):
                break
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes