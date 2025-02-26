def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for start in range(n - 419):
        substring = s[start:start + 420]
        if len(substring) == 420 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes