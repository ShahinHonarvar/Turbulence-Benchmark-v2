def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(6, 9):
        for i in range(10, 75 - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes