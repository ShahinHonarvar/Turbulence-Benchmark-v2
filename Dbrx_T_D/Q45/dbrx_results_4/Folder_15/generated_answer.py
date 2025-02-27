def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, len(s) - 1):
        for j in range(i + 1, min(len(s), i + 3)):
            substring = s[i:j + 1]
            letters = set(substring) & english_letters
            if len(letters) >= 3:
                substring = ''.join(sorted(letters))
                palindromes.add(substring + substring[-1:0:-1])
    return palindromes