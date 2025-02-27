def palindrome_of_length_at_least_n(s):
    English_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 89 and all((c in English_letters for c in substring)) and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes