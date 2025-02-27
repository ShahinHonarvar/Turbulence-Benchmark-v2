def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 8):
        substring = s[i:i + 9].lower()
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes