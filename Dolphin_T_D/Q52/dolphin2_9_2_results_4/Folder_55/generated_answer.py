def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if i + 97 <= len(s):
            substring = s[i:i + 97]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes