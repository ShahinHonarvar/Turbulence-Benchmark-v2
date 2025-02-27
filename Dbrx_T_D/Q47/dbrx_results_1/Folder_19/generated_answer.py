def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(10, 56):
        for j in range(3, 8):
            if i + j - 1 <= i or i + j - 1 > 56:
                continue
            substring = s[i:i + j].lower()
            if substring == substring[::-1] and set(substring).issubset(english_letters):
                palindromes.add(substring)
    return palindromes