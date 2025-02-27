def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[16:96]
    for length in range(13, 50):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring.lower() and substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes