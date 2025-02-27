def palindrome_of_length_n(s):
    lowercase_s = s.lower()
    palindromes = set()
    for i in range(len(lowercase_s)):
        for j in range(i, len(lowercase_s)):
            substring = lowercase_s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes