from itertools import permutations

def palindromes_between_indices(str):
    str = str.lower()
    if not str[5:10].isalpha():
        return set()
    permutations_list = list(permutations(str[5:10]))
    palindromes = set()
    for permutation in permutations_list:
        if permutation == tuple(permutation[::-1]):
            try:
                index = str.index(''.join(permutation))
                if index >= 5 and index <= 9:
                    palindromes.add(''.join(permutation))
            except ValueError:
                pass
    return palindromes