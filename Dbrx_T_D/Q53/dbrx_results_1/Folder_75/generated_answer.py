def palindrome_of_length_at_least_n(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - 39):
        for j in range(i + 40 - len(s), i + 1):
            if s[i:j] and all((c in english_letters for c in s[i:j])) and (s[i:j] == s[i:j][::-1]):
                palindromes.add(s[i:j].lower())
    return palindromes