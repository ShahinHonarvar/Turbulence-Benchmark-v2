def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 33):
        substring = s[i:i + 34]
        if len(substring) == 34 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes