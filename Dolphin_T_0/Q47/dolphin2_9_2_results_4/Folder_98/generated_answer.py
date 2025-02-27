def palindromes_of_specific_lengths(s):
    s = s[0:21]
    palindromes = set()
    for length in range(5, 81):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes