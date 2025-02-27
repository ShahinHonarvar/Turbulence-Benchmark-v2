def palindromes_between_indices(s):
    s = s.lower()
    chars = s[2:10]
    eng_letters = [c for c in chars if c.isalpha()]
    palindromes = set()
    for i in range(len(eng_letters) - 3):
        for j in range(i + 1, len(eng_letters) - 2):
            pal = ''.join(eng_letters[i:j + 1])
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes