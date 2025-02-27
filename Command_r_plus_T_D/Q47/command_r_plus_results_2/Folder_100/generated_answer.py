def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[29:97].lower()
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes