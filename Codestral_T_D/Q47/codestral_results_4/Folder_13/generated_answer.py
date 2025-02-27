def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(57, 61):
        for i in range(13, 96 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes