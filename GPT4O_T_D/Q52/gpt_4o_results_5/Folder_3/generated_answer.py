def palindrome_of_length_n(s):
    normalized_str = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = 100
    length = len(normalized_str)
    for i in range(length - n + 1):
        substring = normalized_str[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes