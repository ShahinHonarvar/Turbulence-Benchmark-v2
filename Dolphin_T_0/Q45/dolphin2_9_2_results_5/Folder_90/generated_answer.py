def palindromes_between_indices(s):
    letters = set(''.join((s[i] for i in range(6) if s[i].isalpha())).lower())
    length = 4
    palindromes = set()
    for p in range(length, len(s) + 1):
        for i in range(len(s) - p + 1):
            sub = set(''.join(s[i:i + p]).lower())
            if letters.issubset(sub) and sub == set(reversed(sub)):
                palindromes.add(''.join(s[i:i + p]))
    return palindromes