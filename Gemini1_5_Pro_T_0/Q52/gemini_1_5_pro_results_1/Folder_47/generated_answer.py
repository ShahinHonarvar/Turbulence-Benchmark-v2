def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes