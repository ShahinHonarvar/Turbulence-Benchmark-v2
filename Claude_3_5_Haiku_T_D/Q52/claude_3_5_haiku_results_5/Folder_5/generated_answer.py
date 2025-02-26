def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 16):
        substring = s[i:i + 17]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes