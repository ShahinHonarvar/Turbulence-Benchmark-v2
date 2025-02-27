def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_in_range = set(s[2:5]).intersection(english_letters)
    if len(letters_in_range) < 2:
        return set()
    palindromes = set()
    for i in range(3, 5):
        for j in range(5 - i + 1):
            candidate = s[j:j + i]
            if candidate == candidate[::-1] and set(candidate).issubset(letters_in_range):
                palindromes.add(candidate.lower())
    return palindromes