def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 3):
        substring = s[i:i + 4]
        if len(substring) == 4 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes