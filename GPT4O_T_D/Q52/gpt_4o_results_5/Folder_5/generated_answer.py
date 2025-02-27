def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s))
    n = len(s)
    for i in range(n - 16):
        substring = s[i:i + 17]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring.lower())
    return palindromes