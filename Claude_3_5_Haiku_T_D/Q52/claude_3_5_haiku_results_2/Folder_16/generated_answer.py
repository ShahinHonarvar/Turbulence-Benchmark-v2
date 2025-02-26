def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 254):
        substring = s[start:start + 255]
        if len(substring) == 255 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes