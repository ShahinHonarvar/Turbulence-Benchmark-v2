def palindromes_between_indices(text):
    substring = text[4:10]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters = {char.lower() for char in substring if char.lower() in english_letters}
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, i):
            word = ''.join(perm)
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes