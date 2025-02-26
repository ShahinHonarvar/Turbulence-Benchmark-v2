def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(substring) == 99 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes