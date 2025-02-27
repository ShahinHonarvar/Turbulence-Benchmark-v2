def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(15, 96):
        for j in range(20, 67):
            if i + j - 1 < len(s) and set(s[i:i + j]) <= english_letters:
                if s[i:i + j].lower() == s[i:i + j][::-1].lower():
                    palindromes.add(s[i:i + j])
    return palindromes