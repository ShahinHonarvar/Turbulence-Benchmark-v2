def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 41):
        substring = s[start:start + 42]
        if len(substring) == 42 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes