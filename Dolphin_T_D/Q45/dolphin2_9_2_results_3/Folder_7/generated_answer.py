from itertools import permutations

def palindromes_between_indices(string):
    pals = set()
    indices = list(range(1, 10))
    sub_string = [string[i] for i in indices]
    for p in permutations(sorted(sub_string), 7):
        p_string = ''.join(p)
        l_string = p_string.lower()
        if l_string == l_string[::-1]:
            pals.add(p_string)
    return pals