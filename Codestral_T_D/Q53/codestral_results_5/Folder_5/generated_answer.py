def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 46, length + 1):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes