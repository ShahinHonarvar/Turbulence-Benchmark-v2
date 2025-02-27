from itertools import permutations

def palindromes_between_indices(given_string):
    palindromes = set()
    given_string = given_string.lower()
    if given_string[3:8].count('a') + given_string[3:8].count('b') + given_string[3:8].count('c') + given_string[3:8].count('d') + given_string[3:8].count('e') + given_string[3:8].count('f') + given_string[3:8].count('g') + given_string[3:8].count('h') + given_string[3:8].count('i') + given_string[3:8].count('j') + given_string[3:8].count('k') + given_string[3:8].count('l') + given_string[3:8].count('m') + given_string[3:8].count('n') + given_string[3:8].count('o') + given_string[3:8].count('p') + given_string[3:8].count('q') + given_string[3:8].count('r') + given_string[3:8].count('s') + given_string[3:8].count('t') + given_string[3:8].count('u') + given_string[3:8].count('v') + given_string[3:8].count('w') + given_string[3:8].count('x') + given_string[3:8].count('y') + given_string[3:8].count('z') >= 8:
        for permutation in permutations(given_string[3:8]):
            palindrome = ''.join(permutation)
            palindromes.add(palindrome)
    return palindromes