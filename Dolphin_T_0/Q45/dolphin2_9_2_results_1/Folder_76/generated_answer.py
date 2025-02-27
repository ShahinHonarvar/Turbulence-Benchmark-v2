def palindromes_between_indices(s):
    letters = [c for c in s[1:5] if c.isalpha()]
    result = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = ''.join(letters[i:j]).lower()
            if sub == sub[::-1] and len(sub) >= 4:
                result.add(sub)
    return result