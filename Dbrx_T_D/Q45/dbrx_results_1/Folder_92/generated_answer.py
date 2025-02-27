def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if len(s) < 8 or not any((char in english_letters for char in s[4:8])):
        return set()
    palindromes = set()
    for i in range(4, 8):
        for j in range(i, 8):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and len(s[i:j + 1]) >= 4:
                palindromes.add(s[i:j + 1])
    return palindromes