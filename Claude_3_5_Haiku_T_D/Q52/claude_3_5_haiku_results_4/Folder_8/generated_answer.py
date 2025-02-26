def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 48):
        substring = s[start:start + 49]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes