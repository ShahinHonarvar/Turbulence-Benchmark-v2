def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, min(5, len(s)) + 1):
        for j in range(i, min(len(s), 5) + 1):
            substring = s[i - 1:j].lower()
            if set(substring) <= english_letters and len(substring) >= 3:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes