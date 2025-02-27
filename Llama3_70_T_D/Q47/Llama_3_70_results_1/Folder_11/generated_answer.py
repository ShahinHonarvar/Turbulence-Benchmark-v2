def palindromes_of_specific_lengths(s):
    s = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes