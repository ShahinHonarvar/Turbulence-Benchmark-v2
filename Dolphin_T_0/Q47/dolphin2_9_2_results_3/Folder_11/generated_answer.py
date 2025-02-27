def palindromes_of_specific_lengths(s):
    s = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes