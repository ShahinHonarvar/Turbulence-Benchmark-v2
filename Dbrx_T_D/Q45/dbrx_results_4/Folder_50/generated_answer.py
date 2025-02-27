def palindromes_between_indices(s):
    english_letters = set((char.lower() for char in s if char.upper() != char.lower()))
    if len(english_letters) == 0 or len(s) < 9:
        return set()
    substr = s[4:9]
    palindromes = set()
    for perm in itertools.permutations(substr, len(substr)):
        candidate = ''.join(perm)
        if candidate.islower() and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes.intersection(english_letters)