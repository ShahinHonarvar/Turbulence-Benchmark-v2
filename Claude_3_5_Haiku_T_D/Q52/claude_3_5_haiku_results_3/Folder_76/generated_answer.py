def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 256):
        substring = s[start:start + 257]
        if len(substring) == 257 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes