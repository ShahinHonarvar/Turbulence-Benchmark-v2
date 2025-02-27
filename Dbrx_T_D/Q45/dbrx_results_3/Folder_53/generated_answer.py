def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[4:9].lower()
    palindromes = set()
    for i in range(6, len(substr) + 1):
        for j in range(len(substr) - i + 1):
            if substr[j:j + i] == substr[j:j + i][::-1] and english_letters.issuperset(substr[j:j + i]):
                palindromes.add(substr[j:j + i])
    return palindromes