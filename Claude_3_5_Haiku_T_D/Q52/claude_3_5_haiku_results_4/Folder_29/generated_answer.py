def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if len(substring) == 19 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes