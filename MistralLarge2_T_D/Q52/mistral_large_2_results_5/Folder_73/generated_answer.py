def palindrome_of_length_n(s):
    length = 41
    palindromes = set()
    s = s.lower()
    n = len(s)
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes