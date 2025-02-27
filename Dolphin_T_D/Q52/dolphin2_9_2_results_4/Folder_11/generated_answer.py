def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 77 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes