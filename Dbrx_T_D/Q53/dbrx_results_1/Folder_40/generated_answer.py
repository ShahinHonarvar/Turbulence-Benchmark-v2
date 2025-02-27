def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for center in range(len(s)):
        for length in range(3, len(s) - center + 1):
            if center - length >= 0 and s[center - length] == s[center]:
                palindrome = s[center - length:center + length + 1]
                if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes