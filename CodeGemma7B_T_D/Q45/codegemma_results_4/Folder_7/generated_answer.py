from itertools import permutations

def palindromes_between_indices(string):
    set_of_palindromes = set()
    for i in range(1, 10):
        for j in range(i + 1, 10):
            temp_set = {''.join(k) for k in permutations(string[i:j + 1])}
            for s in temp_set:
                if s == s[::-1]:
                    set_of_palindromes.add(s.lower())
    if not set_of_palindromes:
        return set()
    return set_of_palindromes