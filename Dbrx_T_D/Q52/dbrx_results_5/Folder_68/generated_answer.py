def palindrome_of_length_n(s):
    s = s.lower()
    n = 76
    palindromes = set()
    for i in range(len(s) - n + 1):
        palindrome = s[i:i + n]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes