def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i, 141):
            substring = s[i:j + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 60 and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes