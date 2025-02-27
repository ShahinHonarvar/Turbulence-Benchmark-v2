def palindrome_of_length_n(s):
    n = 88
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes