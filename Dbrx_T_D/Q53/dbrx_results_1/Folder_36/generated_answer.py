def palindrome_of_length_at_least_n(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and all((c in english_letters for c in s[i:j + 1])) and (len(s[i:j + 1]) >= 144):
                palindromes.add(s[i:j + 1])
    return palindromes