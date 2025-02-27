def palindromes_between_indices(s):
    letters = [char for char in s[:7] if char.isalpha()]
    unique_letters = set(letters.lower())
    if len(unique_letters) >= 3:
        return {letters[i] + letters[i + 1] + letters[i + 2] + letters[i + 2] + letters[i + 1] + letters[i] for i in range(len(letters) - 2)}
    else:
        return set()