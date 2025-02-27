def palindrome_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    res = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            p = letters[i:j + 1]
            if p == p[::-1]:
                res.add(''.join(p))
    return res