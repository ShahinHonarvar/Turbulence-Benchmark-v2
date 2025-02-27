def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 422):
        substring = s[i:i + 423]
        if substring == substring[::-1] and len(substring) == 423:
            palindromes.add(substring)
    return palindromes