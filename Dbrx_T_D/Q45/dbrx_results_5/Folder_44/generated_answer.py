def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[2:8].lower()
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1] and candidate[0] in english_letters:
                palindromes.add(candidate)
    return palindromes