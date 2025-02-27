def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[65:100]
    for i in range(26, 34):
        for j in range(len(substring) - i + 1):
            if all((c.isalpha() for c in substring[j:j + i])) and substring[j:j + i].lower() == substring[j:j + i].lower()[::-1]:
                palindromes.add(substring[j:j + i])
    return palindromes