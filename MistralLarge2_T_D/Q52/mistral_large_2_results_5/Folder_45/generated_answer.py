def palindrome_of_length_n(s):
    n = 21
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes