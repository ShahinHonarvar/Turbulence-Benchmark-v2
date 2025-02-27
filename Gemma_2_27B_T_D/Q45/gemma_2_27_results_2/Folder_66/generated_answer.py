def palindromes_between_indices(text):
    letters = sorted((c for c in text[:6].lower() if c.isalpha()))
    return {''.join(letters[i:i + 5] + letters[i + 4:i:-1]) for i in range(5) if len(letters) >= 5}