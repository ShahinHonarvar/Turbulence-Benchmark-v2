def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 400):
        substring = s[i:i + 401]
        if len(substring) == 401 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes