from itertools import permutations
    import string

def palindromes_between_indices(string):
    n = len(string)
    subset = ''
    start_index = 0
    end_index = 6
    if n > 6:
        subset = string[start_index:end_index + 1]
    else:
        subset = string
    letters = [char.lower() for char in subset if char.isalpha()]
    palindromes = {''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i) if ''.join(p).lower() == ''.join(p[::-1]).lower()}
    return palindromes if palindromes else set()