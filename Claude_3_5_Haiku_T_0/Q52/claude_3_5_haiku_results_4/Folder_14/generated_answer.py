def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(substring) == 63 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes