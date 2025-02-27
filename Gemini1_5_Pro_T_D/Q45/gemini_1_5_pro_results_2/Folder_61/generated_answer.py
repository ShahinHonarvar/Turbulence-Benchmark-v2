from itertools import permutations

def palindromes_between_indices(string):
    letters = set([x.lower() for x in string[:8] if x.isalpha()])
    output = set()
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                output.add(word)
    return output