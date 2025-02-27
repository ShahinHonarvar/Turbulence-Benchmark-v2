def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(12, 57):
        for j in range(i, i + 21):
            if j < len(s) and all((s[k] in english_letters for k in range(i, j + 1))):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    palindromes.add(s[i:j + 1].lower())
    return palindromes