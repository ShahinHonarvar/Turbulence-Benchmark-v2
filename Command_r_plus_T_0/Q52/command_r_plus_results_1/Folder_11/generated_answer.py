def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 76):
        substring = s[i:i + 77]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes