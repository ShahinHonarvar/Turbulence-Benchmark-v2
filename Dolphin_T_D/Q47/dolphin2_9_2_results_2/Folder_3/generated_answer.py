def palindromes_of_specific_lengths(s):
    substring = s[27:96]
    palindromes = set()
    for i in range(49, 52):
        for j in range(len(substring) - i + 1):
            palindrome = substring[j:j + i]
            if palindrome == palindrome.lower() == palindrome.upper() and all([c.isalpha() for c in palindrome]):
                palindromes.add(palindrome)
    return palindromes