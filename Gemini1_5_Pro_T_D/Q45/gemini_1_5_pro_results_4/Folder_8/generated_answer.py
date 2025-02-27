def palindromes_between_indices(text):
    letters = set()
    for i in range(1, 6):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for i in range(len(letters) + 1):
        for j in range(i, len(letters) + 1):
            for subset in itertools.combinations(letters, i):
                for permutation in itertools.permutations(subset, i):
                    word = ''.join(permutation)
                    for k in range(j - i + 1):
                        palindrome = word[:k] + word[::-1] + word[k:]
                        if len(palindrome) >= 5:
                            palindromes.add(palindrome)
    return palindromes