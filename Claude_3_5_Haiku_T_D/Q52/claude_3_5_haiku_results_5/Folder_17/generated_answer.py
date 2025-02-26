def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 288):
        substring = s[i:i + 289]
        if len(substring) == 289 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes