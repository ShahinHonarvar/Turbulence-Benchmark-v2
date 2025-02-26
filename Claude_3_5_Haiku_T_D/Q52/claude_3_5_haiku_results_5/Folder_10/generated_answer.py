def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 53):
        substring = s[start:start + 54]
        if len(substring) == 54 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes