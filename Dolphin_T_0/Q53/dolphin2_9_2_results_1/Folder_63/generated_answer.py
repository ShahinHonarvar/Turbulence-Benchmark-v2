def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 36):
        substring = s[i:i + 37]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes