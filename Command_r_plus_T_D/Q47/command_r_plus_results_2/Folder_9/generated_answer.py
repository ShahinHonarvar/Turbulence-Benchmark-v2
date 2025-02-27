def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(50, 61):
        for j in range(len(s) - i):
            if j <= 300:
                substring = s[j:j + i]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes