def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    target_length = 407
    if n < target_length:
        return palindromes
    for i in range(n - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes