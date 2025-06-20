def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes