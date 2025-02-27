def palindromes_between_indices(s):
    letters = set(s[1:5].lower())
    return {word.lower() for word in letters ** 5 if word == word[::-1]}