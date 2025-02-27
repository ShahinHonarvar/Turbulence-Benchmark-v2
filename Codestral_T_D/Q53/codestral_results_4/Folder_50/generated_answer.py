def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 91
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes