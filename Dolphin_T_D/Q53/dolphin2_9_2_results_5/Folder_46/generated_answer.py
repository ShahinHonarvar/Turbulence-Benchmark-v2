def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = 86
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes