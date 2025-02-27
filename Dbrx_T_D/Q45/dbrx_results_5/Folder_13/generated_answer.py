def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[3:10].lower()
    palindromes = set()
    for i in range(5, len(substr) + 1):
        for j in range(len(substr) - i + 1):
            candidate = substr[j:j + i]
            if candidate in english_letters and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes