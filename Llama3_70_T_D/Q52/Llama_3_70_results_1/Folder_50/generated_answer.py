def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 40 + 1):
        substring = s[i:i + 40]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes