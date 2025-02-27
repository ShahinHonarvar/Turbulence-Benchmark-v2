def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[7:10].lower()
    palindromes = set()
    for i in range(3, 0, -1):
        for j in range(4 - i, len(substr) - i + 1):
            combination = substr[j:j + i]
            if combination == combination[::-1] and english_letters >= set(combination):
                palindromes.add(combination)
    return palindromes