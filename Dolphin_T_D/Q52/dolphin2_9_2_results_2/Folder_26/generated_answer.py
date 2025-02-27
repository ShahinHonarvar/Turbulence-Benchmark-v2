def palindrome_of_length_n(s):
    n = 366
    lowercase_s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = lowercase_s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes