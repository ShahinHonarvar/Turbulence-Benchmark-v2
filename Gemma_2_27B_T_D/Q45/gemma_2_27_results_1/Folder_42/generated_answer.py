def palindromes_between_indices(text):
    substring = text[6:10]
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            candidate = ''.join(letters[i:j + 1]).lower()
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes