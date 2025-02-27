def palindromes_between_indices(s):
    letters = ''.join([ch for ch in s[3:10] if ch.isalpha()])
    letters = letters.lower()
    n = len(letters)
    palindromes = set()
    if n < 7:
        return palindromes
    for length in range(7, n + 1):
        for i in range(n - length + 1):
            word = letters[i:i + length]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes