def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 45):
        substring = s[i:i + 46]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes