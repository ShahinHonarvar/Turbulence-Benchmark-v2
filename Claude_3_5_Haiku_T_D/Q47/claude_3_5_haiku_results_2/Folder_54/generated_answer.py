def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i, 78):
            substring = s[i:j + 1].lower()
            if 18 <= len(substring) <= 19 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes