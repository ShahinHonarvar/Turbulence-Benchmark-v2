def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 3, min(i + 5, 8)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes