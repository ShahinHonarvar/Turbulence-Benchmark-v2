def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 187):
        substring = s[start:start + 188]
        if len(substring) == 188 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes