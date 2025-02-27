def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[3:9].lower()
    palindromes = set()
    for i in range(len(substr) - 4):
        for j in range(i + 5, len(substr) + 1):
            candidate = substr[i:j]
            if candidate and english_letters.issuperset(candidate) and (candidate == candidate[::-1]):
                palindromes.add(candidate)
    return palindromes