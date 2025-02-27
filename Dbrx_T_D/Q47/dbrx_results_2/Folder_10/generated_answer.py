def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(16, 61):
        for j in range(16, 61 - i):
            substring = s[i:i + j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return {p for p in palindromes if len(p) in range(16, 40) and p.isalpha()}