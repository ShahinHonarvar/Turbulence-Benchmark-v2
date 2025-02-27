def palindromes_between_indices(s):
    substring = s[1:5]
    letters = [c for c in substring if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            candidate = letters[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes