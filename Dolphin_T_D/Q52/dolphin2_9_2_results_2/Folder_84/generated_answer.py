def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 131 <= len(s)):
            substring = s[i:i + 131]
            if all((x.isalpha() for x in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes