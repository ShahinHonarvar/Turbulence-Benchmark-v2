def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for i in range(n - 23):
        substring = s[i:i + 24]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes