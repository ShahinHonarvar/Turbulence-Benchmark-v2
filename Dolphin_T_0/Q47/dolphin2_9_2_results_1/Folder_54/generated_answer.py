def palindromes_of_specific_lengths(s):
    s = s[27:77]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes