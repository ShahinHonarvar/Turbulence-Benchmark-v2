def palindromes_between_indices(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if set(substring).issubset(valid_chars):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes