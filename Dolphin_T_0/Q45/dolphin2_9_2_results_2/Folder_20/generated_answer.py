def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[2:9] if ch.isalpha()]
    return {p for i in range(2, len(letters)) for p in [letters[i:i + 2 * j] + letters[i + 2 * j - 1:i - 1:-1] for j in range(2, len(letters) - i + 1) if len(set(p)) < 2]}