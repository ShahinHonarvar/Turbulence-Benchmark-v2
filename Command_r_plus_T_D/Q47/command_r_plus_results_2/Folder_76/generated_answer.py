def palindromes_of_specific_lengths(s: str) -> set:
    s = s[100:293].lower()
    palindromes = set()
    for i in range(154, 183):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes