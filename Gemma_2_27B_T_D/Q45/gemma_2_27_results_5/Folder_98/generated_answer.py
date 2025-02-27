def palindromes_between_indices(s):
    letters = s[3:6].lower()
    return {candidate for candidate in {'abba', 'baab', 'caba', 'abac', 'baac'} if set(candidate).issubset(set(letters)) and len(candidate) >= 4}