def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 181 + 1):
        substring = s[i:i + 181]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes