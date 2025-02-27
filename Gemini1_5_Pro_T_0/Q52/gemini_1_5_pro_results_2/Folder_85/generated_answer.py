def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes