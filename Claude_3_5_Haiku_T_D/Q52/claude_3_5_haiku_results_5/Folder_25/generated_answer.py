def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(substring) == 90 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes