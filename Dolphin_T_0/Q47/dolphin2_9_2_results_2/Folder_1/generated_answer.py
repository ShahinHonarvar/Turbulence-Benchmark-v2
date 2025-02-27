def palindromes_of_specific_lengths(s):
    substring = s[15:90]
    palindromes = set()
    for i in range(40, 73):
        for palindrome in set((substring[x:x + i] for x in range(0, len(substring) - i + 1))):
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome.lower())
    return palindromes