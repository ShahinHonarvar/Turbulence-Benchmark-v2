def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(s) - length + 1):
            palindrome = s[i:i + length]
            if palindrome.isalpha() and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes