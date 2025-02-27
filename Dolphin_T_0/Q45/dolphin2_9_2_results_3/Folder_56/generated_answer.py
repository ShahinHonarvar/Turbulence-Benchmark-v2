def palindromes_between_indices(s):
    letters_between = s[5:10]
    palindrome_set = set()
    for p in range(5, 100):
        for w in combinations(letters_between, p):
            word = ''.join(w)
            if word.lower() == word.lower()[::-1] and len(word) >= 5:
                palindrome_set.add(word.lower())
    return palindrome_set