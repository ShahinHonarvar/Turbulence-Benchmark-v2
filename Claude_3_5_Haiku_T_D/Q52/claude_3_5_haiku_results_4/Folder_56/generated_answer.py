def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 95
    for start in range(len(s) - n + 1):
        substring = s[start:start + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes