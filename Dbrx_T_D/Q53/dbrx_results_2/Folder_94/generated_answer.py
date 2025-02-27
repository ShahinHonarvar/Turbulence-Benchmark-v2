def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 40):
        for j in range(i + 41, len(s) + 1, 2):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes