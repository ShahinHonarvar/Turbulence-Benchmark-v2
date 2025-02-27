def palindrome_of_length_at_least_n(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and s[i:j + 1].lower() in english_letters and (len(s[i:j + 1]) >= 56):
                palindromes.add(s[i:j + 1])
    return palindromes