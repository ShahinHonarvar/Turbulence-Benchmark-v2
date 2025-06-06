def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes