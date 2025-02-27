from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = set()
    for i in range(2, 5):
        letter = s[i].lower()
        if letter.isalpha():
            letters.add(letter)
    palindromes = set(chain.from_iterable((permutations(letters, i + 2) for i in range(1, min(len(letters), 3)))))
    return {''.join(p) for p in palindromes if ''.join(p) == ''.join(reversed(p))}