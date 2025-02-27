def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = set((s[i:j + 1].lower() for i in range(7) for j in range(i, 7)))
    palindromes = {sub for sub in substr if sub == sub[::-1] and len(sub) >= 5 and all((letter in english_letters for letter in sub))}
    return palindromes