def palindromes_of_specific_lengths(s: str) -> set[str]:
    palindromes = set()
    substring = s[64:100].lower()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes