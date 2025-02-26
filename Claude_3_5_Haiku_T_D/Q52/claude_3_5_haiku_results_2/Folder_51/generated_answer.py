def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(substring) == 73 and substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes