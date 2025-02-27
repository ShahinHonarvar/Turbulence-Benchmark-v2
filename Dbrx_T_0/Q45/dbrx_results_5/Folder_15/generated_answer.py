def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, len(s)):
        for j in range(i, min(len(s), i + 3)):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes