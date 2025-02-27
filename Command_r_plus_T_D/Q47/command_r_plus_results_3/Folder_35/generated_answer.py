def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[33:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes