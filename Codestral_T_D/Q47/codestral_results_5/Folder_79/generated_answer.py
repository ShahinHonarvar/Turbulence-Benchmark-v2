def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 3, i + 5):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes