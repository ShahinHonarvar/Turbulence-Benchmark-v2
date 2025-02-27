def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(34, 56):
        for i in range(30, len(s) - length + 1):
            palindrome = s[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes