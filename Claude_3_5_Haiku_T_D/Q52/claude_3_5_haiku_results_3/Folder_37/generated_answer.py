def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if len(substring) == 84 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes