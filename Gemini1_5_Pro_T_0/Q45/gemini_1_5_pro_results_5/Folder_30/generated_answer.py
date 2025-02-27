from itertools import permutations

def palindromes_between_indices(string):
    letters = set([x.lower() for x in string[:5] if x.isalpha()])
    output = set()
    for i in range(4, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                output.add(word)
    return output