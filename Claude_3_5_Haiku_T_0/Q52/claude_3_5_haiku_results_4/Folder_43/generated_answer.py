def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 50):
        substring = s[i:i + 51]
        if len(substring) == 51 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes