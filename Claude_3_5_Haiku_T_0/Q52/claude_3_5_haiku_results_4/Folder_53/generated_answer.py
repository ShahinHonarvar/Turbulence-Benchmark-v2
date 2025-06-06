def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(substring) == 68 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes