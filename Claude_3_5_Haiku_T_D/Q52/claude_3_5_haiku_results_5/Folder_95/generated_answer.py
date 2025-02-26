def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 86):
        substring = s[start:start + 87]
        if len(substring) == 87 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes