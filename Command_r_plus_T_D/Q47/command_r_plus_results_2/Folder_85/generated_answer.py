def palindromes_of_specific_lengths(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(30, 99):
        for j in range(i - 5, i + 3):
            if j < 0 or j >= len(s):
                continue
            substring = s[j:i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes