def palindromes_between_indices(s):
    chars = [c for c in s[0:7] if c.isalpha()]
    palindromic_words = set()
    for a in chars:
        for b in chars:
            for c in chars:
                for d in chars:
                    word = a + b + c + d
                    if word == word[::-1]:
                        palindromic_words.add(word.lower())
    return palindromic_words