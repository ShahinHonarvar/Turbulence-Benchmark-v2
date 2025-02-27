def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(12, 57):
        for j in range(i + 20, i + 23):
            if j <= 56 and all((char in english_letters for char in s[i:j])):
                if s[i:j][::-1] == s[i:j]:
                    palindromes.add(s[i:j])
    return palindromes