def palindromes_between_indices(s):
    letters = sorted(s[2:5].lower())
    palindromes = set()
    if len(letters) >= 4:
        for i in range(len(letters) - 3):
            for j in range(i + 1, len(letters) - 2):
                for k in range(j + 1, len(letters) - 1):
                    for l in range(k + 1, len(letters)):
                        palindrome = ''.join([letters[i], letters[j], letters[k], letters[l], letters[l], letters[k], letters[j], letters[i]])
                        palindromes.add(palindrome)
    return palindromes