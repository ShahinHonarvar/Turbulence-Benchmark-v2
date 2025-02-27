def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(13, 67):
        for index in range(11, len(s) - length + 2):
            palindrome = s[index:index + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes