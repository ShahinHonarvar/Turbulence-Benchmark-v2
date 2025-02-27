def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for j in range(18, 20):
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes