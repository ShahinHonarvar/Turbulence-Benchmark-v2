def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    return {s.lower() for i in range(len(letters)) for j in range(i, len(letters) + 1) if letters[i:j + 1] == letters[i:j + 1][::-1] and j - i + 1 > 2}