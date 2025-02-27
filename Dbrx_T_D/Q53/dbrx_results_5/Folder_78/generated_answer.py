def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) >= 96 and set(substring).issubset(set('abcdefghijklmnopqrstuvwxyz')):
                palindromes.add(substring)
    return palindromes