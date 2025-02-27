def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[6:10]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i, len(substr)):
            candidate = substr[i:j + 1]
            if candidate and all((letter in english_letters for letter in candidate)) and (candidate == candidate[::-1]):
                palindromes.add(candidate.lower())
    return {p for p in palindromes if len(p) >= 3}