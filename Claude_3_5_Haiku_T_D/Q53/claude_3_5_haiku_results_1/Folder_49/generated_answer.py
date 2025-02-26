def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) >= 73 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes