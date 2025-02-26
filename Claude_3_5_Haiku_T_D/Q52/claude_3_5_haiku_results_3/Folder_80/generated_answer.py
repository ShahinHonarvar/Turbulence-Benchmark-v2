def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    target_length = 276
    for start in range(n):
        for end in range(start + target_length, n + 1):
            substring = s[start:end]
            if len(substring) == target_length and substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes