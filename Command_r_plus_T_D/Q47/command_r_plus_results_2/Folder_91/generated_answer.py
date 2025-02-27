def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    s_lower = s[:11].lower()
    for i in range(len(s_lower)):
        for j in range(i + 3, min(i + 6, len(s_lower) + 1)):
            substring = s_lower[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes