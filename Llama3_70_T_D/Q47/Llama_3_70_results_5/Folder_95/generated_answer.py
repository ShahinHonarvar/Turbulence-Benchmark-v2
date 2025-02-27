def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes