def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6]]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            sub = ''.join(letters[i:j + 1])
            if len(sub) >= 3 and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes