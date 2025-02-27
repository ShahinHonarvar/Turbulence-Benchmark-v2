def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    english_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(154, 183):
        for j in range(len(s) - i + 1):
            if s[j:j + i] not in english_letters:
                continue
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes