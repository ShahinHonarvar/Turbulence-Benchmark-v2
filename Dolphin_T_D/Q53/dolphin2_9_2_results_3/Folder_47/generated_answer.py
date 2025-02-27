def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(77, 0, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes