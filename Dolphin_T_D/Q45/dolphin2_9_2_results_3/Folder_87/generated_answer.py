def palindromes_between_indices(s):
    letter_set = set([c for c in s[3:10] if c.isalpha()])
    return set([word for word in letter_set if len(word) >= 3 and word == word[::-1]])