def palindrome_of_length_n(s):
    palindromes = set()
    length = 39
    s = s.lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes