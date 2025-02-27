def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(23, 40):
        for index in range(31, 75 - length + 1):
            palindrome = s[index:index + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes