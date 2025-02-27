def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 17, len(s) + 1):
            substring = s[i:j]
            if all((x.isalpha() for x in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes