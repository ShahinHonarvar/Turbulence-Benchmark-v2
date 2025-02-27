def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    length = len(letters)
    palindromes = set()
    for i in range(length):
        for j in range(i + 5, length):
            sub = letters[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes