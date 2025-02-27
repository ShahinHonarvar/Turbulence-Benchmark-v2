def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length - 44):
        substring = s[i:i + 45]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes