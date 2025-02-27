def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(17, 73):
        for j in range(i - 50, i - 49):
            if j < 0:
                continue
            substring = s[i:j:-1]
            if all((c in english_letters for c in substring)) and s[i] == s[j - 1] and (substring == substring[::-1]):
                palindromes.add(s[i:j])
    return palindromes