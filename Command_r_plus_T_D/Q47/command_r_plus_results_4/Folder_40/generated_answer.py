def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s = s[:6].lower()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 6, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes