def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            palindrome = s[i:j + 1]
            if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 13:
                palindromes.add(palindrome)
    return palindromes