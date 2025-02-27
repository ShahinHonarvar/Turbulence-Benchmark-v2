def palindromes_between_indices(s):
    s = s[4:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(6, len(s) + 1):
        for j in range(len(s) - i + 1):
            candidate = s[j:j + i]
            if set(candidate) <= english_letters and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes