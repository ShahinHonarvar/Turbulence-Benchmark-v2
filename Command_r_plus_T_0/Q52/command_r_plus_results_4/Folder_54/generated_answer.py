def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 84):
        substring = s[i:i + 85]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes