def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 7):
        for j in range(i, 7):
            sub = s[i - 1:j].lower()
            if sub.isalpha() and len(sub) >= 4 and (set(sub) <= english_letters):
                palindromes.add(sub[::-1] + sub[1:])
    return palindromes