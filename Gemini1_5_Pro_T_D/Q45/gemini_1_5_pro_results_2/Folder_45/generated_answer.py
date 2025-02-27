import itertools

def palindromes_between_indices(string):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    relevant_letters = []
    for i in range(5, 10):
        if string[i].lower() in english_letters:
            relevant_letters.append(string[i].lower())
    palindromes = set()
    for i in range(4, len(relevant_letters) + 1):
        for item in itertools.permutations(relevant_letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes