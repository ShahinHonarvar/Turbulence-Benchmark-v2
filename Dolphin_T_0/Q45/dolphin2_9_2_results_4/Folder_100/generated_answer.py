from itertools import permutations, chain

def palindromes_between_indices(s):
    exports = set()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    temp = ''
    for i in range(6):
        temp += alphabet[alphabet.index(s[i].lower())]
    combinations = chain.from_iterable((permutations(temp, r) for r in range(6, len(temp) + 1)))
    for com in combinations:
        palin = ''.join(com)
        if palin == palin[::-1]:
            exports.add(palin)
    return exports