def palindromes_between_indices(s):
    letters = s[7:10].lower()
    return {s[i:j + 1] for i in range(len(letters)) for j in range(i, len(letters)) if letters[i:j + 1] == letters[i:j + 1][::-1] and len(letters[i:j + 1]) >= 3}