def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 59, len(s)):
            substring = s[i:j + 60]
            if substring == substring[::-1] and all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring)):
                palindromes.add(substring)
    return palindromes