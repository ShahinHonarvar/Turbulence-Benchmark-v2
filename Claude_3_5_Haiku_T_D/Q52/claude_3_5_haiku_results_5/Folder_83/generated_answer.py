def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 23):
        substring = s[start:start + 24]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes