def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if len(substring) == 53 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes