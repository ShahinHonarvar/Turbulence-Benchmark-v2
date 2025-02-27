def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 5, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring.lower())
    return palindromes