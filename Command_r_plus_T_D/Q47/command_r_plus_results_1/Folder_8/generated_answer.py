def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[16:73].lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(i + 51, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes