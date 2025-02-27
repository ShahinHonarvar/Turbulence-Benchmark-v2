from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    sub_string = string[2:8].lower()
    for p in permutations(sub_string):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes