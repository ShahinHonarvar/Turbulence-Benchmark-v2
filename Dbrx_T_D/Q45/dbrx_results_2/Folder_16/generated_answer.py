def palindromes_between_indices(s):
    s = s[6:10].lower()
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters = eng_letters.intersection(set(s))
    palindromes = set()
    for j in range(5, len(s) + 1):
        for i in range(len(s) - j + 1):
            if s[i:i + j] == s[i:i + j][::-1] and set(s[i:i + j]).issubset(letters):
                palindromes.add(s[i:i + j])
    return palindromes