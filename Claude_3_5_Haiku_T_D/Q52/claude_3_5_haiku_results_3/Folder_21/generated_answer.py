def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 406):
        substring = s[i:i + 407]
        if len(substring) == 407 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes