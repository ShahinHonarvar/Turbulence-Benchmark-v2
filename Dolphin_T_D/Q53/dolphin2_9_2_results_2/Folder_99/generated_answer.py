def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 114):
        substring = s[i:i + 115]
        if all((c.isalpha() for c in substring)):
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes