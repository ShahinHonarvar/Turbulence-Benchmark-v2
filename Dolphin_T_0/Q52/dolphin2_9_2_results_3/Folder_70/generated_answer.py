def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = 401
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes