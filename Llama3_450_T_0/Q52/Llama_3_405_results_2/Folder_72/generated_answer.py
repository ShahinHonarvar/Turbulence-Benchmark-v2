def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes