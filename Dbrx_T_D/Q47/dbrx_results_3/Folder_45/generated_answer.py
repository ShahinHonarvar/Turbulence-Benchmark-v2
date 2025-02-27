def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(3, 61):
        for index in range(70, 141 - length):
            substring = s[index:index + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes