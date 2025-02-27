def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(5, 81):
        for index in range(20 - length + 1):
            substring = s[index:index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes