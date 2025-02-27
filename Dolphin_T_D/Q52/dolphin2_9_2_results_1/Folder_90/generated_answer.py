def palindrome_of_length_n(s):
    s = s.lower()
    n = 318
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes