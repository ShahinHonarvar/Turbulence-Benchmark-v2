def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 91 + 1):
        substring = s[i:i + 91]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes