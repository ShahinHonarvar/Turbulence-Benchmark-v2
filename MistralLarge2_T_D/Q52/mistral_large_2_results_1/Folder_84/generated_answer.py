def palindrome_of_length_n(s):
    n = 131
    palindromes = set()
    s = s.lower()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes