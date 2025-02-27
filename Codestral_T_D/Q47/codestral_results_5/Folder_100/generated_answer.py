def palindromes_of_specific_lengths(s):
    s = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes