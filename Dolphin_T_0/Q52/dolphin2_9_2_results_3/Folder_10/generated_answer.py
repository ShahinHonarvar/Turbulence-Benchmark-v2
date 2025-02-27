def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 53):
        substring = s[i:i + 55]
        if substring == substring[::-1] and all((char.isalpha() for char in substring)):
            palindromes.add(substring)
    return palindromes