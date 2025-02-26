def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(substring) == 94 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes