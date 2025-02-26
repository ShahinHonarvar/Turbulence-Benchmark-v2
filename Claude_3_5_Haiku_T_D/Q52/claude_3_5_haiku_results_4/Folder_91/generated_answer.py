def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if len(substring) == 7 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes