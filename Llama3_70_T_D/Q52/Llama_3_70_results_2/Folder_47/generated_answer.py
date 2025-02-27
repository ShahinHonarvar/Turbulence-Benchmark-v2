def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 34, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes