def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(6):
        for j in range(i, 6):
            substring = s[i:j + 1].lower()
            if set(substring).issubset(english_letters) and len(substring) >= 3:
                if substring == substring[::-1]:
                    result.add(substring)
    return result