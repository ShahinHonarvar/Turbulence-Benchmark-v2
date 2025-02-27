def palindromes_between_indices(s):
    substring = s[1:5]
    unique_letters = set(''.join((''.join(e) for e in substring.split())))
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for p in unique_letters:
            for q in unique_letters:
                palindromes.add(p.upper() + q.upper() + p.lower())
    return palindromes