def palindrome_of_length_at_least_n(s):
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    n = 77
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if all((c in english_letters for c in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes