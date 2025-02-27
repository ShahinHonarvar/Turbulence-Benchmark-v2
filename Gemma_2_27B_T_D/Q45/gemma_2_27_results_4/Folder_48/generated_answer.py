def palindromes_between_indices(text):
    letters = sorted([c for c in text[6:9] if c.isalpha()])
    palindromes = set()
    if len(letters) >= 4:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        palindrome = ''.join([letters[i], letters[j], letters[k], letters[l], letters[l], letters[k], letters[j], letters[i]])
                        palindromes.add(palindrome.lower())
    return palindromes