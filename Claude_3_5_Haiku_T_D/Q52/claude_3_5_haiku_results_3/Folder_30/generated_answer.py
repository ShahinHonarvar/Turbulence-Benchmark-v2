def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 93):
        substring = s[start:start + 94]
        if len(substring) == 94 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes