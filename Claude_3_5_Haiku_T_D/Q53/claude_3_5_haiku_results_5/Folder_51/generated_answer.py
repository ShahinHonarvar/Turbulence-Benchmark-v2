def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 63
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes