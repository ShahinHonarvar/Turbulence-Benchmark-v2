def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 25):
        substring = s[i:i + 26]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes