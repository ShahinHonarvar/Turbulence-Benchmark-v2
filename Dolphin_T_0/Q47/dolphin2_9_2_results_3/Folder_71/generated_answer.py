def palindromes_of_specific_lengths(s):
    s = s[17:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes