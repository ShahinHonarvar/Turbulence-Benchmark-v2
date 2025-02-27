from itertools import permutations

def palindromes_between_indices(txt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = set()
    for i, j in zip(range(0, 8), range(7, -1, -1)):
        if txt[i] in alphabet and txt[j] in alphabet:
            first, last = (txt[i], txt[j])
            mid = txt[i + 1:j]
            for letters in permutations(mid):
                output.add(first + ''.join(letters) + last)
    return output