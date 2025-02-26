def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    if n < 66:
        return palindromes
    for i in range(n - 65):
        substring = s[i:i + 66]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes