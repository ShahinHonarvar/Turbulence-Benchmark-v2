def palindromes_between_indices(s):
    english_letters = ''.join((c for c in s[1:10] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 1, len(english_letters) - (i + 6 - 1)):
            substring = english_letters[i:j] + english_letters[j:i - 1:-1]
            if len(substring) >= 7:
                palindromes.add(substring)
    return palindromes