def palindrome_of_length_n(s):
    palindromes = set()
    n = 289
    normalized_s = ''.join((char.lower() for char in s if char.isalpha()))
    for i in range(len(normalized_s) - n + 1):
        substring = normalized_s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes