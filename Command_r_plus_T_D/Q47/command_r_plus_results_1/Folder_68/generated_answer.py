def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[:51].lower()
    palindromes = set()
    for i in range(len(s) - 49):
        for j in range(50, 101):
            if j + i > len(s):
                break
            substring = s[i:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes