def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 87):
        substring = s[i:i + 88]
        if len(substring) == 88 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes