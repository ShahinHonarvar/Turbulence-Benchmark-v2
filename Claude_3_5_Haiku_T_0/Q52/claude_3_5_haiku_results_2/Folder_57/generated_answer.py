def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(substring) == 92 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes