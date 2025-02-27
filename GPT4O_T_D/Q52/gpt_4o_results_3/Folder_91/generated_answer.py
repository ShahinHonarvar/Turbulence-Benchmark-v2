def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if substring == substring[::-1]:
            palindromes.add(s[i:i + 7])
    return palindromes