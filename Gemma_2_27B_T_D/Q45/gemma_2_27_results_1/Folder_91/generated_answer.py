def palindromes_between_indices(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = {letter for letter in text[2:7].lower() if letter in alphabet}
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, i):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes