def palindrome_of_length_n(s):
    length = 74
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + length, i + length + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes