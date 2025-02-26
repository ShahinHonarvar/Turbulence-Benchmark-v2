def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 71):
        substring = s[i:i + 72]
        if len(substring) == 72 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes