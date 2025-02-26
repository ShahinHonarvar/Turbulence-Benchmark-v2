def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 53):
        substring = s[i:i + 54]
        if len(substring) == 54 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes