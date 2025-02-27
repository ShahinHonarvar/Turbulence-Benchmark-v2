def palindrome_of_length_n(s):
    English_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if set(substring).issubset(English_letters):
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes