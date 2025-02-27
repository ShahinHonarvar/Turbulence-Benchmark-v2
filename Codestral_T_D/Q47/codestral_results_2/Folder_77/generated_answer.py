def palindromes_of_specific_lengths(s):
    s = s[103:277].lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for l in range(100, 170):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1] and set(sub) <= alphabet:
                palindromes.add(sub)
    return palindromes