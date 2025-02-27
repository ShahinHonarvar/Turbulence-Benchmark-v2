def palindromes_between_indices(s):
    letters = ''.join(sorted(s[1:4]))
    palindromes = set()
    for i in range(1 << len(letters)):
        pal = ''
        for j in range(len(letters)):
            if i & 1 << j != 0:
                pal += letters[j]
        if len(pal) >= 4 and pal == pal[::-1]:
            palindromes.add(pal.lower())
    return palindromes