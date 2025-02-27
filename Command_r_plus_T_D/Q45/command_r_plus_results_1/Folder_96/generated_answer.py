def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[3:9])
    palindromes = set()
    for letter in s_letters:
        if letter in english_letters:
            s_letters.add(letter.swapcase())
    for i in range(6, 13):
        for perm in permutations(s_letters, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes