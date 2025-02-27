def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 75):
        for j in range(6, 9):
            substring = s[i:i + j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes