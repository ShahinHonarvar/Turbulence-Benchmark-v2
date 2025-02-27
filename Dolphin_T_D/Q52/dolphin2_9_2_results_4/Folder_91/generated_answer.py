def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s)):
            substring = s[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes