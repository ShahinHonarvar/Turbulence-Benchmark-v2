def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(33, 86):
        for j in range(26, 32):
            palindrome = s[i:i + j].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes