def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) == 39:
                palindromes.add(substring.lower())
    if not palindromes:
        return set()
    else:
        return palindromes