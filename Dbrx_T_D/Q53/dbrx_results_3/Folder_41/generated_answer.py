def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 27):
        for j in range(i + 14, len(s)):
            palindrome = s[i:j + 1]
            if palindrome == palindrome[::-1] and len(palindrome) >= 28:
                palindromes.add(palindrome)
    return palindromes