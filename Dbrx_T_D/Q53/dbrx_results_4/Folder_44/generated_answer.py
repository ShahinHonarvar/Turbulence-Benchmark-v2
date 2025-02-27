def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            palindrome = s[i:j + 1]
            if len(palindrome) >= 89 and palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes