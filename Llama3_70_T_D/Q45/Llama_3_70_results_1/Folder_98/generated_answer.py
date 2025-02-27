def palindromes_between_indices(s):
    s = s[3:6].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    if len(letters) < 2:
        return result
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            first_half = letters[i] + letters[j]
            result.add(first_half + first_half[::-1])
            for k in range(len(letters)):
                if k != i and k != j:
                    result.add(first_half + letters[k] + first_half[::-1])
    return result