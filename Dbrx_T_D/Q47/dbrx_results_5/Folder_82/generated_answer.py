def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(30, 301):
        for index in range(3, len(s) - length + 1):
            substring = s[index:index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes