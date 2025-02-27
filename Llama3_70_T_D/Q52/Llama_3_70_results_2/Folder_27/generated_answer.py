def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes