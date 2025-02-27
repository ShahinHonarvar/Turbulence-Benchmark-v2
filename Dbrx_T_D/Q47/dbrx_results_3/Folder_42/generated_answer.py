def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(18, 48):
        for start in range(43, 96 - length + 1):
            palindrome = s[start:start + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes