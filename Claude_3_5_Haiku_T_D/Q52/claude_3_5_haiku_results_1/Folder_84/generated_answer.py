def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 130):
        substring = s[i:i + 131]
        if len(substring) == 131 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes