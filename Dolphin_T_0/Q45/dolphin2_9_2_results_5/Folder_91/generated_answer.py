def palindromes_between_indices(s):
    letters = ''.join(sorted(s[2:7]))
    res = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            if letters[i:j].lower() == letters[i:j].lower()[::-1]:
                res.add(letters[i:j].lower())
    return res