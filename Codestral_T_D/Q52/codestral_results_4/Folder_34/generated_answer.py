def palindrome_of_length_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length - 32):
        substring = s[i:i + 33].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes