def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length - 27):
        substring = s[i:i + 28]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes