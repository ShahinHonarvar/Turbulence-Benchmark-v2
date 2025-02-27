def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(12, 15):
        for start in range(18, 89 - length + 1):
            palindrome = s[start:start + length].lower()
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes