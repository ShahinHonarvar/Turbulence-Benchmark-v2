def palindrome_of_length_n(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 48 + 1):
        substring = s[i:i + 48]
        if len(substring) < 48:
            continue
        if any((char not in english_letters for char in substring)):
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes