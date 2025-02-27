def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(min(6, len(s))):
        for j in range(max(0, i + 3 - len(s)), i + 1):
            substring = s[i:j].lower()
            if set(substring).issubset(english_letters) and substring == substring[::-1]:
                result.add(substring)
    return result