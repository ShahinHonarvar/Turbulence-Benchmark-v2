def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if len(substring) == 96 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes