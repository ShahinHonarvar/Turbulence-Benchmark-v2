def palindrome_of_length_n(s):
    s = s.lower()
    n = 407
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.islower():
            palindromes.add(substring)
    return palindromes