def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            palindrome = s[i:i + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes