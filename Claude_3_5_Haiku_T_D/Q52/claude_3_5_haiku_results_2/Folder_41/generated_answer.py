def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 59):
        substring = s[start:start + 60]
        if len(substring) == 60 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes